'''
Todo I2C guard to only read if ADAU1701 is confirmed confgured.
'''

from cfg import *
from hardware import adau1701 as DSP
from threading import Thread
import time

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
        self._vol_hysteres = 3  # volume error margin
        self._pwr_state = GPIO.input(PWR_EN_12V_PIN)
        self._vol_error = 0
        self._true_vol = self._get_hw_volume()

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
        if t_now - self._t_last_dsp_read > 1 / self._dps_sample_freq_lim:
            self._t_last_dsp_read = t_now
            with i2c_lock:  # ensure safe i2s read
                self._true_vol = int(float(DSP.read_back(_ADD_VOL_READBACK_HIGH, _ADD_VOL_READBACK_LOW)) * 100)
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
            vol_err = abs(vol - vol_now)
            if vol_err <= self._vol_hysteres:
                # Error is within margin
                self._hw_vol_stop()
                return True

            # increase volume of to low or decrease if to high
            self._hw_vol_move(dir=vol_now < vol)

            time.sleep(0.001 * vol_err)

            # Ensure that error is decreasing
            if 0 < self._vol_error <= vol_err:
                time.sleep(0.75 + 1 / self._dps_sample_freq_lim)  # Ensure new dsp reading
                vol_now = self._get_hw_volume()
                vol_err = abs(vol - vol_now)
                if vol_err >= self._vol_error:
                    # Volume error not improving
                    log.err('HW vol error not decreasing!')
                    return False
            else:
                t_start = time.perf_counter()
            self._vol_error = vol_err
        log.err('HW vol timeout')
        self._hw_vol_stop()
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
                if vol != self._req_vol:  # Volume change
                    self._req_vol = vol
                    self.emit_volume = True
                self._volume_master = (None, 'Manual')[self.emit_volume]  # Master is Manual until no longer emit volume

            # Software volume change
            elif self._req_vol != self._true_vol:
                self.emit_volume = True
                if not self._set_hw_volume(self._req_vol):
                    # unable to change true volume
                    self._req_vol = self._true_vol

            # sleep for time proportional to update frequency of for 1 sec if in standby
            t_sleep = (max(1 / self._update_freq - dt, 0.01), 1)[standby]
            time.sleep(t_sleep)

    def _hw_vol_move(self, dir):
        """
        Change hw volume position
        :param dir: increase if true else decrease
        :return: None
        """
        dt = time.perf_counter() - self._t_last_dsp_read
        # Ensure limit is not reached
        if dir and self._true_vol < 100 or not dir and self._true_vol > 0:
            if dt < 5:
                self._pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
                GPIO.output(PWR_EN_12V_PIN, 1)
                DIR = ((0, 1), (1, 0))[dir]
                GPIO.output([VOL_UP_PIN, VOL_DN_PIN], DIR)
            else:
                log.err('New HW volume read required!')
        else:
            log.err('Volume limit reached!')

    def _hw_vol_stop(self):
        GPIO.output([VOL_UP_PIN, VOL_DN_PIN], 0)
        GPIO.output(PWR_EN_12V_PIN, self._pwr_state)  # restore power state


"""
class Volume:
    def __init__(self, sw_vol=0, hw_vol=0, balance=0):
        self.hw_volume = hw_vol  # Actual volume
        self.sw_volume = sw_vol  # Set software volume
        self.volume = hw_vol  # Requested Volume
        self.balance = balance
        self.activity = False
        self.update_frequency = 1
        self._t_scan = time.perf_counter()
        self._vol_hysteres = 3
        self._rising_vol = True
        self._pwr_state = GPIO.input(PWR_EN_12V_PIN)
        self._vol_error = 0
        self.running = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        self.running = True
        t.start()
        return self

    def run(self):
        self.running = True
        while self.running:
            self.update_volume()

    def update_volume(self, f=None):
        if not f:
            f = self.update_frequency
        if time.perf_counter() - self._t_scan >= 1 / f:

            # Manual volume change
            # Set volume to HW volume
            if GPIO.input(ACTIVITY_PIN) and self.volume == self.sw_volume:
                self.activity = True
                self.volume = self.hw_volume
            # Software volume change
            # Set volume and HW volume to SW volume
            elif self.sw_volume != self.volume:
                foo = self.set_hw_vol(self.sw_volume)  # is blocking until volume error is 0
                self.volume = self.hw_volume
                time.sleep(0.1)

            if self.activity:
                return True
        return False

    def hw_vol_up(self):
        self._pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
        GPIO.output(PWR_EN_12V_PIN, 1)
        GPIO.output([VOL_UP_PIN, VOL_DN_PIN], (GPIO.HIGH, GPIO.LOW))

    def hw_vol_dn(self):
        self._pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
        GPIO.output(PWR_EN_12V_PIN, 1)
        GPIO.output([VOL_UP_PIN, VOL_DN_PIN], (GPIO.LOW, GPIO.HIGH))

    def hw_vol_stop(self):
        GPIO.output([VOL_UP_PIN, VOL_DN_PIN], 0)
        GPIO.output(PWR_EN_12V_PIN, self._pwr_state)  # restore power state

    def get_hw_vol(self):
        _t_scan = time.perf_counter()
        vol = int(float(DSP.read_back(_ADD_VOL_READBACK_HIGH, _ADD_VOL_READBACK_LOW)) * 100)
        # Higher sensitively in turning direction and lower in opposite direction.
        if self._rising_vol and (vol > self.hw_volume or (vol + 1) < self.hw_volume) or \
                (vol < self.hw_volume or (vol - 1) > self.hw_volume):
            _update_hw_vol_freq = 100
            self._rising_vol = self.hw_volume < vol
            self.hw_volume = vol
            log.info("HW Volume: {}%".format(self.hw_volume))
            self._vol_error = abs(self.sw_volume - self.hw_volume)
            self.activity = True
        else:
            _update_hw_vol_freq = 1.9
            self.activity = False
        return self.hw_volume

    def set_hw_vol(self, vol=None):
        _TIMEOUT = 1
        if vol is None:
            vol = self.sw_volume
        t_now = time.time()
        vol_now = self.get_hw_vol()

        # approx time to reach vol
        t_dif = abs(vol - vol_now)

        # while not timed out, try to set volume
        while t_now + _TIMEOUT * t_dif + 0.5 > time.time():
            vol_now = self.get_hw_vol()
            new_vol_err = abs(vol - vol_now)
            if self._vol_error < self._vol_hysteres:
                self.hw_vol_stop()
                return True
            elif vol_now < vol:
                self.hw_vol_up()
            else:
                self.hw_vol_dn()

            # Check if error is decreasing
            if new_vol_err >= self._vol_error:
                time.sleep(0.75)
                vol_now = self.get_hw_vol()
                new_vol_err = abs(vol - vol_now)
                if new_vol_err >= self._vol_error:
                    self.hw_vol_stop()
                    log.err('HW vol error!')
                    return False
            self._vol_error = new_vol_err

            time.sleep(0.5 * self._vol_error)
        self.hw_vol_stop()
        return False

"""

if __name__ == '__main__':
    vol_request = 50
    VOL = VolumeController().start()
    VOL.set_volume(vol_request, timeout=10)
    while True:
        if VOL.emit_volume:
            print(VOL.get_volume())
            VOL.emit_volume = False
        time.sleep(0.1)
