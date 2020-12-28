# Todo:
#  I2C guard to only read if ADAU1701 is confirmed configured.
#  Make Volume controller separate process
#  Use i2c_lock for locking i2c and volume_event for indicating new event

import multiprocessing as mp
from hardware import adau1701 as DSP
from threading import Thread
import time
import numpy as np
from socketIO_client import SocketIO
from modules.shared import *
from cfg import *


class VolumeController:
    VOL_REG = divmod(VOLUME_READ_REG, 0x100)

    def __init__(self, init_volume=None):
        """
                Volume controller
        """
        self.is_alive = False
        self._t_last_dsp_read = 0
        self._vol_change = False  # todo remove
        self._vol_event_timeout = 2  # todo implement
        self._vol_error = 0  # todo remove
        self._update_freq = 10  # todo remove

        # MP variables
        self._true_vol = mp.Value('i', 0)
        self._target_vol = mp.Value('i', init_volume) if init_volume is not None else mp.Value('i', 0)
        self.read_hw_volume()

        # controller setup
        self.Kp = 10
        self.Ki = 0
        self.Kd = 0
        self.vol_up = None
        self.vol_dn = None
        self._hw_vol_request_event = mp.Event()
        self._hw_vol_finish_event = mp.Event()
        self.shutdown_event = mp.Event()
        self.i2s_lock = i2c_lock
        self.vol_ctrl_process = mp.Process(name='volume controller',
                                           target=self._vol_controller)

    def start(self):
        if not self.is_alive:
            self.is_alive = True
            self.vol_ctrl_process.start()
            return self

    def stop(self, join=False):
        if self.is_alive:
            self.is_alive = False
            self._hw_vol_request_event.set()
            self.shutdown_event.set()
            if join:
                self.vol_ctrl_process.join()
            return True
        return False

    def set_volume(self, vol, timeout=None):
        """
        Check if valud volume request. If so, update target volume and set volume event request.
        :param vol:
        :param timeout:
        :return:
        """
        # Ensure new volume request
        if vol == self.get_volume():
            return True

        # Ensure valid volume request
        if not 0 <= vol <= 100:
            log.err('Unsupported volume. Range is [0 - 100]')
            return False

        # Ensure controller process ir running
        if not self.is_alive:
            log.err('Volume controller not started!')
            return False

        if timeout is None:
            timeout = self._vol_event_timeout

        with self._target_vol.get_lock():
            self._target_vol.value = vol

        # if timeout is 0, no hardware actuation is requested
        if timeout <= 0:
            return True

        # Register new volume request
        ret = False
        # reset finish flag
        if self._hw_vol_finish_event.is_set():
            self._hw_vol_finish_event.clear()
        self._hw_vol_request_event.set()

        # Activate power for potentiometer motor
        pwr12v.set()
        if self._hw_vol_finish_event.wait(timeout=timeout):
            ret = True
        pwr12v.release()

        return ret

    def get_volume(self):
        """
        Volume getter
        :return: Get true volume
        """
        with self._true_vol.get_lock():
            return self._true_vol.value

    def read_hw_volume(self):
        """
        Read actual DSP volume if dt > 100ms
        :return: DSP volume [0-100]
        """
        t_now = time.perf_counter()
        if t_now - self._t_last_dsp_read > 1 / 10:  # todo check smallest possible sampling freq
            self._t_last_dsp_read = t_now
            with i2c_lock:  # ensure safe i2s read
                # get DSP (Potentiometer) volume
                vol = float(DSP.read_back(VolumeController.VOL_REG[0], VolumeController.VOL_REG[1])) * 100

            with self._true_vol.get_lock():
                self._true_vol.value = int(vol)

            return vol
        return self.get_volume()

    # ############ Process functions ############

    def _vol_controller(self):
        """
        Multiprocessing volume controller.
        Activated by a volume event
        :param _vol_target: Multiprocessing value of target volume
        :param _vol_event:  Multiprocessing volume Event
        :return:
        """
        # GPIO setup
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([VOL_UP_PIN, VOL_DN_PIN], GPIO.OUT)
        GPIO.setup(ACTIVITY_PIN, GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup(PWR_EN_12V_PIN, GPIO.IN)

        # Setup PWM
        vol_up = GPIO.PWM(VOL_UP_PIN, 500)
        vol_dn = GPIO.PWM(VOL_DN_PIN, 500)
        vol_up.start(0)
        vol_dn.start(0)

        timeout = self._vol_event_timeout

        def hw_vol_move(delta):
            """
            Change hw volume position
            :param delta: increase or decrease volume change
            :return: True if successful, else False
            """
            if delta == 0:
                return True
            dt = time.perf_counter() - self._t_last_dsp_read
            # Ensure limit is not reached

            # update hw volume
            true_vol = self.read_hw_volume()

            if true_vol < 100 and delta > 0 or delta < 0 and true_vol > 0:
                if dt < 1:
                    speed = abs(delta)
                    # pin_pos, pin_neg = ([vol_up, vol_dn], [vol_dn, vol_up])[change < 0]
                    pin_pos, pin_neg = [vol_up, vol_dn] if delta > 0 else [vol_dn, vol_up]
                    pin_pos.ChangeDutyCycle(speed)
                    pin_neg.ChangeDutyCycle(0)
                    return True
                else:
                    log.err('New HW volume read required!')  # todo change to mp err code
            else:
                log.err('Volume limit reached!')  # todo change to mp err code
            hw_vol_stop()
            return False

        def hw_vol_stop():
            vol_up.ChangeDutyCycle(0)
            vol_dn.ChangeDutyCycle(0)

        def dsp_activity_callback(channel):
            # global act_event
            act = GPIO.input(channel)
            act_event.set() if act else act_event.clear()

        # hw volume acquisition thread setup
        act_event = Event()

        # Add dsp activity event detection
        GPIO.add_event_detect(ACTIVITY_PIN, GPIO.BOTH, dsp_activity_callback)

        def acquisition_thread(ftx, hw_event):
            hw_event.wait()
            ftx.read_hw_volume()

        Thread(target=acquisition_thread, args=(self, act_event,), daemon=True).start()

        while not self.shutdown_event.is_set():

            # wait for new volume event
            if not self._hw_vol_request_event.wait(timeout=1):
                continue

            I = 0
            last_err = 0
            dt = 1
            t_start = t_last = time.perf_counter()
            while time.perf_counter() - t_start <= timeout and GPIO.input(PWR_EN_12V_PIN):

                time.sleep(max(0.0, 0.1 - dt))  # todo ensure constant time execution

                # get new target
                with self._target_vol.get_lock():
                    vol_target = self._target_vol.value

                # get time delta
                t_now = time.perf_counter()
                dt = t_now - t_last
                t_last = t_now

                vol_true = self.read_hw_volume()

                err = vol_target - vol_true
                abs_err = abs(err)

                if abs_err < 0.5:  # target within round-of
                    hw_vol_stop()
                    break

                D = (last_err - err) / dt
                change = np.clip(err * self.Kp + I * self.Ki + D * self.Kd, -100, 100)
                hw_vol_move(change)
                I += err * dt
                last_err = err

                # Ensure decreasing error.
                if 0 <= abs(last_err) < abs_err:
                    if time.perf_counter() - t_last > 2:
                        # Volume error not improving for 2 sec, break
                        log.err('HW-vol not decreasing!')  # todo change to mp error code
                        hw_vol_stop()
                        break
                else:
                    t_start = time.perf_counter()  # Error decreasing, reset timeout
            self._hw_vol_finish_event.set()  # Indicate volume event finished
            self._hw_vol_request_event.clear()  # Volume event done clear volume event to wait for next.

        # Shutdown event Set
        vol_up.stop()
        vol_dn.stop()
        self._hw_vol_finish_event.set()  # release all waiting listeners
        if self._hw_vol_request_event.is_set():
            self._hw_vol_request_event.clear()


class VOLUME:

    def __init__(self, init_volume=None, emit_volume_func=None):
        """
                Volume event handler
        :param init_volume: startup volume if defined, else hw volume
        """
        # extrinsics
        self.emit_vol_func = emit_volume_func  # Function called at new volume event. format: func(volume, source)
        self.is_alive = False

        # intrinsics
        self._t_last_dsp_read = 0
        self._vol_change = False  # todo remove
        self._vol_event_timeout = 2
        self._vol_error = 0  # todo remove
        self._update_freq = 10  # todo remove

        # source manager
        self._volume_master = None  # Volume source master, Only master can change volume until target is met
        self.vol_event = Event()
        self.shutdown_event = Event()
        self._manager_thread = Thread(name="volume manager",
                                      target=self._vol_manager)

        # Volume controller
        self.volume_controller = VolumeController(init_volume)

    def start(self):
        if not self.is_alive:
            self.is_alive = True
            self.volume_controller.start()
            self._manager_thread.start()
            return self

    def stop(self, join=False):
        if self.is_alive:
            self.is_alive = False
            self.shutdown_event.set()
            self.volume_controller.stop(join)
            if join:
                self._manager_thread.join()
            return True
        return False

    def set_volume(self, vol, src=None, timeout=None, bypass=False):
        """
        Check if volume is ready to be changed
        Then assign volume change event to master source
        (Prevent other sources to change volume until target is met or timeout)
        :param bypass: force new volume master
        :param timeout: Timeout for volume change event
        :param vol: Volume request
        :param src: Source requesting change, if not selected, change is not protected
        :return: True if successful volume event, else False
        """
        if vol == self.get_volume():
            return True

        if not 0 <= vol <= 100:
            log.err('Unsupported volume. Range is [0 - 100]')
            return False

        if timeout is None:
            timeout = self._vol_event_timeout

        if self._volume_master in [src, None] or bypass:
            self._volume_master = src
            return self.volume_controller.set_volume(vol, timeout)

        return False

    def get_volume(self):
        """
        Volume getter
        :return: Get requested volume
        """
        return self.volume_controller.get_volume()

    def get_volume_source(self):
        """
        Get volume event source
        :return: Volume event source if active, else None
        """
        return self._volume_master

    def _vol_manager(self):
        t_last = time.perf_counter()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ACTIVITY_PIN, GPIO.IN)
        dt = 1
        while self.is_alive and not self.shutdown_event.is_set():

            # sleep for time proportional to update frequency or for 1 sec if in standby
            t_sleep = (max(1 / self._update_freq - dt, 0.0), 1)[standby]
            time.sleep(t_sleep)

            # Update time variables
            _t_now = time.perf_counter()
            dt = _t_now - t_last
            t_last = _t_now

            # Get hw activity
            _dsp_activity = GPIO.input(ACTIVITY_PIN)

            """ Handle volume change """  # todo communicate with controller
            # Manual volume change
            if _dsp_activity and self._volume_master in [None, 'Manual']:
                vol = self._get_hw_volume()
                if abs(vol - self._req_vol) >= 1:  # Volume change
                    self._req_vol = vol
                    self.emit_vol_func(vol, self._volume_master)
                self._volume_master = (None, 'Manual')[self.emit_volume]  # Master is Manual until no longer emit volume

            # Software volume change
            elif abs(self._req_vol - self.true_vol) >= 0.5:
                # self.emit_volume = True
                if self._set_hw_volume(self._req_vol):
                    self.emit_volume = True
                else:
                    # unable to change true volume
                    log.warn('Unable to set volume ')
                    self._req_vol = self.true_vol
            # Clear master when no more activity
            elif not _dsp_activity:
                self._volume_master = None

        self.stop()


class VOLUME2:

    def __init__(self, init_volume=None, emit_volume_func=None):
        """
                Volume event handler
        :param init_volume: startup volume if defined, else hw volume
        """
        # extrinsics
        self.emit_vol_func = emit_volume_func  # Function called at new volume event. format: func(volume, source)
        self.is_alive = False
        self.emit_volume = True

        # intrinsics
        self._t_last_dsp_read = 0
        self._vol_change = False  # todo remove
        self._vol_event_timeout = 2
        self._hw_activity_timeout = 1
        self._vol_error = 0  # todo remove
        self._update_freq = 10  # todo remove

        # source manager
        self._volume_master = None  # Volume source master, Only master can change volume until target is met
        self.vol_event = Event()
        self.shutdown_event = Event()
        self._hw_activity_manager = Thread(name="HW activity manager",
                                           target=self._hw_activity_handler)

        # Volume controller
        self.volume_controller = VolumeController(init_volume)

    def start(self):
        if not self.is_alive:
            self.is_alive = True
            self.volume_controller.start()
            self._hw_activity_manager.start()
            return self

    def stop(self, join=False):
        if self.is_alive:
            self.is_alive = False
            self.shutdown_event.set()
            self.volume_controller.stop(join)
            if join:
                self._hw_activity_manager.join()
            return True
        return False

    def set_volume(self, vol, src=None, timeout=None, bypass=False):
        """
        Check if volume is ready to be changed
        Then assign volume change event to master source
        (Prevent other sources to change volume until target is met or timeout)
        :param bypass: force new volume master
        :param timeout: Timeout for volume change event
        :param vol: Volume request
        :param src: Source requesting change, if not selected, change is not protected
        :return: True if successful volume event, else False
        """

        if timeout is None:
            timeout = self._vol_event_timeout

        # only register event of volume master is None or already src.
        if self._volume_master in [src, None] or bypass:
            self._volume_master = src
            # push volume request to volume controller. Returns True if new volume event is registered, else False.
            is_new_event = self.volume_controller.set_volume(vol, timeout)

            if is_new_event and self.emit_vol_func is not None:
                self.emit_vol_func(vol, self._volume_master)

            # event done, reset volume master
            self._volume_master = None

            return is_new_event

        return False

    def get_volume(self):
        """
        Volume getter
        :return: Get requested volume
        """
        return self.volume_controller.get_volume()

    def get_volume_source(self):
        """
        Get volume event source
        :return: Volume event source if active, else None
        """
        return self._volume_master

    def _hw_activity_handler(self):
        """
        Monitor thread for hw activity
        :return: None
        """
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ACTIVITY_PIN, GPIO.IN)
        while self.is_alive and not self.shutdown_event.is_set():

            # wait for hw activity for 2 sec. If no activity, continue.
            if not GPIO.wait_for_edge(ACTIVITY_PIN, GPIO.RISING, timeout=2000):
                continue

            # check if volume event
            if self._volume_master in [None, 'Manual']:
                t_call = time.perf_counter()
                while time.perf_counter() - t_call < self._hw_activity_timeout and GPIO.input(ACTIVITY_PIN):
                    vol = self.get_volume()
                    if abs(vol - self.get_volume()) >= 0.5:  # Volume change
                        # Set new volume.
                        # timeout=0 indicate no hw actuation requested.
                        self.emit_volume = self.set_volume(vol, src='Manual', timeout=0)
                        if self.emit_vol_func is not None:
                            self.emit_vol_func(vol, self._volume_master)
                self._volume_master = None

            # check if EQ event
            # todo


if __name__ == '__main__':
    from socketIO_client import SocketIO

    amp_always_off = True  # disable AMP for debugging

    vol_request = 20

    # setup SPDIF activation to ensure i2s functionality
    GPIO.setup(SPDIF_ENABLE_PIN, GPIO.OUT)
    GPIO.setup(SPDIF_LOCK_PIN, GPIO.IN, GPIO.PUD_UP)
    GPIO.output(SPDIF_ENABLE_PIN, not GPIO.input(SPDIF_LOCK_PIN))
    time.sleep(1)

    VOL = VOLUME2().start()
    VOL.set_volume(vol_request, src='master', timeout=2)


    def vol_ctrl(data):
        vol = data.get('volume', -1)
        source = data.get('service', None)
        if vol != -1:
            VOL.set_volume(vol, src=source, timeout=10)


    def _receive_thread():
        volumioIO.wait()


    volumioIO = SocketIO(volumio_host, volumio_port)

    receive_thread = Thread(target=_receive_thread, name="Receiver", daemon=True)
    receive_thread.start()
    volumioIO.on('pushState', vol_ctrl)
    try:
        while True:
            vol = int(round(VOL.get_volume()))
            act = str(GPIO.input(ACTIVITY_PIN))
            print('Volume: ' + str(vol) + '\nDPS act: ' + act)
            if VOL.emit_volume:
                volumioIO.emit('volume', vol)
                VOL.emit_volume = False
            time.sleep(1)
    except KeyboardInterrupt:
        VOL.stop()
