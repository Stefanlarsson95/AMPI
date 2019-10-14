

from hardware import adau1701 as DSP
from modules import logger
import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
_VOL_READBACK_HIGH = 0x00
_VOL_READBACK_LOW = 0xA6
log = logger.Log()
GPIO.setup([23, 15, 16], GPIO.OUT)
GPIO.output([23, 15, 16], 0)


emit_volume = True
_update_hw_vol_freq = 10
_t_scan = time.time()
hw_volume = 0
sw_volume = 0
balance = 0
vol_err = 0
_VOL_ERR_HYSTERES = 2


def update_volume():
    while True:
        if time.time() - _t_scan >= 1/_update_hw_vol_freq:
            get_hw_vol()


def hw_vol_up():
    GPIO.output(23, 1)
    GPIO.output([15, 16], (GPIO.HIGH, GPIO.LOW))


def hw_vol_dn():
    GPIO.output(23, 1)
    GPIO.output([15, 16], (GPIO.LOW, GPIO.HIGH))


def hw_vol_stop():
    GPIO.output([15, 16], 0)


def get_hw_vol():
    global _t_scan, hw_volume, sw_volume, vol_err, emit_volume
    _t_scan = time.time()
    vol = int(float(DSP.read_back(_VOL_READBACK_HIGH, _VOL_READBACK_LOW))*101)
    if vol != hw_volume:
        hw_volume = vol
        log.info("HW Volume: {}%".format(hw_volume))
        vol_err = abs(sw_volume - hw_volume)
        emit_volume = True
    return hw_volume


def set_hw_vol(vol=-1):
    global vol_err
    _TIMEOUT = 0.05
    if vol == -1:
        vol = sw_volume
    t_now = time.time()
    vol_now = get_hw_vol()

    # approx time to reach vol
    t_dif = abs(vol - vol_now)

    # while not timed out, try to set volume
    while t_now + _TIMEOUT * t_dif + 0.5 > time.time():
        v_now = get_hw_vol()
        new_vol_err = abs(vol - vol_now)
        if vol_err < _VOL_ERR_HYSTERES:
            hw_vol_stop()
            return True
        elif v_now < vol:
            hw_vol_up()
        else:
            hw_vol_dn()

        # Check if mechanical error
        if new_vol_err >= vol_err:
            time.sleep(0.75)
            if new_vol_err >= vol_err:
                hw_vol_stop()
                break
        vol_err = new_vol_err

        time.sleep(0.005*vol_err)
    hw_vol_stop()
    return False
