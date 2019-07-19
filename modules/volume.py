
from hardware import adau1701 as DSP
from threading import Thread
from modules import logger
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
_VOL_READBACK_HIGH = 0x00
_VOL_READBACK_LOW = 0xA6
log = logger.Log()
GPIO.setup([23, 15, 16], GPIO.OUT)
GPIO.output([23, 15, 16], 0)



class VOLUME:
    def __init__(self, volume=-1, balance=0):
        self.LOG_LEVEL = logger.LOGLEVEL.INFO
        log.lvl = self.LOG_LEVEL
        #self._update_hw_interval = 1
        self.update_hw_vol_freq = 1
        self._t_scan = time.time()
        self._hw_volume = self.get_hw_vol()
        if volume == -1:
            self.sw_volume = self._hw_volume
        self.balance = balance
        self.vol_err = 0
        self._VOL_ERR_HYSTERES = 2

    def run(self):
        if time.time() - self._t_scan >= 1/self.update_hw_vol_freq:
            self.get_hw_vol()

    def hw_vol_up(self):
        GPIO.output(23, 1)
        GPIO.output([15, 16], (GPIO.HIGH, GPIO.LOW))

    def hw_vol_dn(self):
        GPIO.output(23, 1)
        GPIO.output([15, 16], (GPIO.LOW, GPIO.HIGH))

    def hw_vol_stop(self):
        GPIO.output([15, 16], 0)

    def get_hw_vol(self):
        self._t_scan = time.time()
        self._hw_volume = int(float(DSP.read_back(_VOL_READBACK_HIGH, _VOL_READBACK_LOW))*101)
        log.info("HW Volume: {}%".format(self._hw_volume))
        try:
            self.vol_err = abs(self.sw_volume - self._hw_volume)
        except Exception as err:
            self.vol_err = 0
            log.err("".format(err))
        log.debug("SW/HW Volume diff: {}".format(self.vol_err))
        return self._hw_volume

    def set_hw_vol(self, vol=-1):
        _TIMEOUT = 0.05
        if vol == -1:
            vol = self.sw_volume
        t_now = time.time()
        vol_now = self.get_hw_vol()

        # approx time to reach vol
        t_dif = abs(vol - vol_now)

        # while not timed out, try to set volume
        while t_now + _TIMEOUT * t_dif + 0.5 > time.time():
            v_now = self.get_hw_vol()
            new_vol_err = abs(vol - vol_now)
            if self.vol_err < self._VOL_ERR_HYSTERES:
                self.hw_vol_stop()
                return True
            elif v_now < vol:
                self.hw_vol_up()
            else:
                self.hw_vol_dn()

            # Check if mechanical error
            if new_vol_err >= self.vol_err:
                time.sleep(0.75)
                if new_vol_err >= self.vol_err:
                    self.hw_vol_stop()
                    break
            self.vol_err = new_vol_err

            time.sleep(0.005*self.vol_err)
        self.hw_vol_stop()
        return False
