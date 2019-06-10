
from hardware import adau1701 as DSP
import RPi.GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BCM)

VOL_READBACK_HIGH = 0x00
VOL_READBACK_LOW = 0xA6


class Volume:
    def __init__(self, volume, hw_volume=0, sw_volume=0, balance=0):

        self.hw_volume = hw_volume
        if sw_volume == 0:
            self.sw_volume = self.hw_volume
        else:
            self.sw_volume = sw_volume
        self.volume = hw_volume
        self.balance = balance
        '''Setup outputs'''
        GPIO.setup([23, 15, 16], GPIO.OUT)
        GPIO.output([23, 15, 16], (GPIO.HIGH, GPIO.LOW, GPIO.LOW))

    def hw_vol_up(self):
        GPIO.output([15, 16], (GPIO.HIGH, GPIO.LOW))

    def hw_vol_dn(self):
        GPIO.output([15, 16], (GPIO.LOW, GPIO.HIGH))

    def hw_vol_stop(self):
        GPIO.output([15, 16], (GPIO.LOW, GPIO.LOW))

    def set_sw_vol(self,volume):
        self.sw_volume = volume

    def get_sw_vol(self):
        return self.sw_volume

    def get_volume(self):
        return self.volume

    def get_hw_vol(self):
        return float(DSP.read_back(VOL_READBACK_HIGH, VOL_READBACK_LOW))*100

    def set_hw_vol(self, vol=-1):
        TIMEOUT = 0.05
        HYSTERES = 2
        if vol == -1:
            vol = self.volume
        t_now = time.time()
        ret = False
        v_now = self.get_hw_vol()
        t_dif = abs(vol - v_now)
        '''while not timed out, try to set volume'''
        while t_now + TIMEOUT * t_dif + 0.5 > time.time() and not ret:
            print "time:", (t_now + TIMEOUT * t_dif + 0.5 - time.time()),
            v_now = self.get_hw_vol()
            dif = abs(vol - v_now)
            if dif < HYSTERES:
                self.hw_vol_stop()
                ret = True
            elif v_now < vol:
                self.hw_vol_up()
            else:
                self.hw_vol_dn()
            t = 0.005 * dif
            time.sleep(0.005*dif)
            print "delay:", t
        self.hw_vol_stop()
        return ret






def main():
    vol = Volume(0)
    t = time.time()
    val = 0

    res = vol.set_hw_vol(val)
    if res:
        print "Successfull volue adjust"
    else:
        print "Error setting value:", val
    print(vol.get_hw_vol())

'''
    while t + 0.5 > time.time():
        print(vol.get_hw_vol())
        vol.hw_vol_dn()
    vol.hw_vol_stop()
    time.sleep(1)

    t = time.time()
    while t + 0.5 > time.time():
        print(vol.get_hw_vol())
        vol.hw_vol_up()
    vol.hw_vol_stop()
'''


if __name__ == '__main__':
    main()