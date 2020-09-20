'''
Todo I2C guard to only read if ADAU1701 is confirmed confgured.
'''

from hardware import adau1701 as DSP
from threading import Thread
import time
from socketIO_client import SocketIO
from cfg import *

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# fixme combine hi/lo addressing to one
_ADD_VOL_READBACK_HIGH = VOLUME_READ_REG >> 8
_ADD_VOL_READBACK_LOW = VOLUME_READ_REG & 0x00ff


class VolumeController:
    def __init__(self, vol=0, bal=0):
        """
        Main Volume class
        :param vol: Initial volume
        :param bal: Initial balance
        """
        self.emit_volume = False  # Indicate volume event
        self.is_alive = False  # Indicate whether volume thread is running

        self._dps_sample_freq_lim = DSP_SAMPLE_FREQ_LIM
        self._req_vol = vol  # target volume
        self._balance = bal
        self._t_last_dsp_read = 0
        self._vol_change = False
        self._volume_master = None  # Volume source master, Only master can change volume until target is met
        self._vol_event_timeout = 5
        self._update_freq = 10  # tread update frequency
        self._vol_hysteres = 0  # volume error margin
        self._pwr_state = None
        self._vol_error = 0
        self._true_vol = self._get_hw_volume()
        self._new_reading = False

    def start(self, daemon=True):
        """
        Start Volume controller Thread
        :param daemon: Run as daemon, def True
        :return: Self
        """
        t = Thread(target=self._vol_controller, name='volume controller thread')
        t.daemon = daemon
        t.start()
        return self

    def stop(self):
        if self.is_alive:
            self.is_alive = False
            return True
        return False

    def set_volume(self, vol, source=None, timeout=None):
        """
        Check if volume is ready to be changed
        Then assign volume change event to master source
        (Prevent other sources to change volume until target is met or timeout)
        :param timeout: Timeout for volume change event
        :param vol: Volume request
        :param source: Source requesting change, if not selected, change is not protected
        :return: True if new volume change event initiated, else false
        """
        if not 0 <= vol <= 100:
            log.err('Unsupported volume. Range is [0 - 100]')
            return False
        if timeout:
            self._vol_event_timeout = timeout

        if self._volume_master in [source, None]:
            self._volume_master = source
            self._req_vol = vol
        else:
            return False
        return True

    def set_balance(self, balance, source=None):
        if balance == 0:
            return True
        log.err('Balance adjust not implemented')
        return False

    def get_volume(self):
        """
        Volume getter
        :return: Get requested volume
        """
        return self._req_vol

    def get_volume_source(self):
        """
        Get volume event source
        :return: Volume event source if active, else None
        """
        return self._volume_master

    def get_balance(self):
        return self._balance

    def _get_hw_volume(self):
        """
        Get actual DSP volume if dt > sample freq lim
        else return last true vol
        :return: DSP volume [0-100]
        """
        t_now = time.perf_counter()
        self._new_reading = t_now - self._t_last_dsp_read > 1 / self._dps_sample_freq_lim
        if self._new_reading:
            self._t_last_dsp_read = t_now
            with i2c_lock:  # ensure safe i2s read
                self._true_vol = float(DSP.read_back(_ADD_VOL_READBACK_HIGH, _ADD_VOL_READBACK_LOW)) * 100
        return self._true_vol

    def _set_hw_volume(self, vol=None, timeout=None):
        """
        Try setting HW volume to requested volume
        :param timeout: Timeout proportional to volume change
        :param vol: Requested volume
        :return: True if target is within margin, else False
        """
        if vol is None:
            vol = self._req_vol
        if timeout is None:
            timeout = self._vol_event_timeout
        t_start = time.perf_counter()

        # while not timed out, try to set volume
        while t_start + timeout > time.perf_counter():
            vol_now = self._get_hw_volume()
            if not self._new_reading:
                continue
            vol_err = abs(vol - vol_now)
            if int(vol_err) <= self._vol_hysteres:  # target met
                # Error is within margin
                self._hw_vol_stop()
                vol_now = self._get_hw_volume()
                self._vol_error = abs(vol - vol_now)
                return True

            # increase volume of to low or decrease if to high
            err = vol - vol_now
            sign = (-1, 1)[err > 0]
            change = sign * max((abs(err) * 5, 100)[abs(err) > 20], 10)  # todo imp integral action
            self._hw_vol_move(change=change)

            t_sleep = max(0.01 * vol_err, 0.5)
            time.sleep(t_sleep)
            self._hw_vol_stop()

            # Ensure that error is decreasing

            if 0 < int(self._vol_error) <= int(vol_err):
                # Volume error not improving
                log.err('HW-vol error not decreasing!')
                return False
            else:
                t_start = time.perf_counter()
            self._vol_error = vol_err
        log.err('HW-vol timeout')
        return False

    def _vol_controller(self):
        t_last_control = time.perf_counter()
        self.is_alive = True
        while self.is_alive:
            # Update time variables
            _t_now = time.perf_counter()
            dt = _t_now - t_last_control
            t_last_control = _t_now

            # Get hw activity status
            _hw_vol_activity = GPIO.input(ACTIVITY_PIN)

            # Handle volume change:
            # Manual volume change
            if _hw_vol_activity and self._volume_master in [None, 'Manual']:
                vol = self._get_hw_volume()
                if abs(vol - self._req_vol) > 1:  # Volume change
                    self._req_vol = vol
                    self.emit_volume = True
                self._volume_master = (None, 'Manual')[self.emit_volume]  # Master is Manual until no longer emit volume

            # Software volume change
            elif self._req_vol != int(self._true_vol):
                self.emit_volume = True
                if not self._set_hw_volume(self._req_vol):
                    # unable to change true volume
                    pass
                    # self._req_vol = self._true_vol
            else:
                self._volume_master = None

            # sleep for time proportional to update frequency of for 1 sec if in standby
            t_sleep = (max(1 / self._update_freq - dt, 0.01), 1)[standby]
            time.sleep(t_sleep)

    def _hw_vol_move(self, change):
        """
        Change hw volume position
        :param change: increase or decrease volume change
        :return: True if successful, else False
        """
        if not change:
            return
        dt = time.perf_counter() - self._t_last_dsp_read
        # Ensure limit is not reached
        if change > 0 and self._true_vol < 100 or change < 0 and self._true_vol > 0:
            if dt < 5:
                if self._pwr_state is None:
                    self._pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
                speed = abs(change)
                pin_a, pin_b = ([vol_up, vol_dn], [vol_dn, vol_up])[change < 0]
                pin_a.ChangeDutyCycle(speed)
                pin_b.ChangeDutyCycle(0)
                GPIO.output(PWR_EN_12V_PIN, GPIO.HIGH)
                return True
            else:
                log.err('New HW volume read required!')
        else:
            log.err('Volume limit reached!')
        self._hw_vol_stop()
        return False

    def _hw_vol_stop(self):
        # GPIO.output([VOL_UP_PIN, VOL_DN_PIN], 0)
        vol_up.ChangeDutyCycle(0)
        vol_dn.ChangeDutyCycle(0)
        if self._pwr_state is None:
            return
        GPIO.output(PWR_EN_12V_PIN, self._pwr_state)  # restore power state
        self._pwr_state = None


if __name__ == '__main__':
    GPIO.output(SPDIF_ENABLE_PIN, 1)
    vol_request = 20
    VOL = VolumeController().start()
    VOL.set_volume(vol_request, source='master', timeout=10)
    volumioIO = SocketIO(volumio_host, volumio_port)

    def vol_ctrl(data):
        vol = data.get('volume', -1)
        if vol != -1:
            VOL.set_volume(vol, 'Volumio', timeout=10)

    def _receive_thread():
        volumioIO.wait()
    receive_thread = Thread(target=_receive_thread, name="Receiver").start()
    volumioIO.on('pushState', vol_ctrl)
    try:
        while True:
            vol = int(VOL._true_vol)
            print(vol)
            if VOL.emit_volume:
                volumioIO.emit('volume', vol)
                VOL.emit_volume = False
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
