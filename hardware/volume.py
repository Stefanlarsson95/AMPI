
from hardware import adau1701 as DSP
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

'''
volume: local target volume
hw_volume: hardware volume
'''
class VOLUME:
    def __init__(self, volume=-1, balance=0):
        self.VOL_READBACK_HIGH = 0x00
        self.VOL_READBACK_LOW = 0xA6
        self.HYSTERES = 2
        self.update_hw_interval = 1
        self.t_scan = time.time()
        self.hw_volume = self.get_hw_vol()
        if volume == -1:
            self.volume = self.hw_volume
        self.balance = balance
        self.err = 0
        '''Setup outputs'''
        GPIO.setup([23, 15, 16], GPIO.OUT)
        GPIO.output([23, 15, 16], 0)

    def hw_vol_up(self):
        GPIO.output(23, 1)
        GPIO.output([15, 16], (GPIO.HIGH, GPIO.LOW))


    def hw_vol_dn(self):
        GPIO.output(23, 1)
        GPIO.output([15, 16], (GPIO.LOW, GPIO.HIGH))

    def hw_vol_stop(self):
        GPIO.output([15, 16], 0)

    def get_volume(self):
        return self.volume

    def get_hw_vol(self):
        self.t_scan = time.time()
        self.hw_volume = int(float(DSP.read_back(self.VOL_READBACK_HIGH, self.VOL_READBACK_LOW))*100)
        try:
            self.err = abs(self.volume - self.hw_volume)
        except:
            self.err = 0
        return self.hw_volume

    def set_hw_vol(self, vol=-1):
        TIMEOUT = 0.05
        if vol == -1:
            vol = self.volume
        t_now = time.time()
        ret = False
        v_now = self.get_hw_vol()
        t_dif = abs(vol - v_now)
        '''while not timed out, try to set volume'''
        while t_now + TIMEOUT * t_dif + 0.5 > time.time() and not ret:
            v_now = self.get_hw_vol()
            self.err = abs(vol - v_now)
            if self.err < self.HYSTERES:
                self.hw_vol_stop()
                ret = True
            elif v_now < vol:
                self.hw_vol_up()
            else:
                self.hw_vol_dn()
            time.sleep(0.005*self.err)
        self.hw_vol_stop()
        return ret
