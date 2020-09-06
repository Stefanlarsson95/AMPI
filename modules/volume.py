'''
Todo I2C guard to only read if ADAU1701 is confirmed confgured.
'''

from cfg import *
from hardware import adau1701 as DSP
from modules import logger
import time

_ADD_VOL_READBACK_HIGH = VOLUME_READ_REG >> 8
_ADD_VOL_READBACK_LOW = VOLUME_READ_REG & 0x00ff
log = logger.Log()


emit_volume = True
_update_hw_vol_freq = 1
_t_scan = time.perf_counter()
hw_volume = 0
sw_volume = 0
balance = 0
vol_err = 0
_VOL_ERR_HYSTERES = 3
rising_vol = True  # Defines the direction of volume knob rotation
_pwr_state = GPIO.input(PWR_EN_12V_PIN)


def update_volume(f=None):
    if not f:
        f = _update_hw_vol_freq
    if time.perf_counter() - _t_scan >= 1/f:
        get_hw_vol()
        if emit_volume:
            return True
    return False


def hw_vol_up():
    global _pwr_state
    _pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
    GPIO.output(PWR_EN_12V_PIN, 1)
    GPIO.output([VOL_UP_PIN, VOL_DN_PIN], (GPIO.HIGH, GPIO.LOW))


def hw_vol_dn():
    global _pwr_state
    _pwr_state = GPIO.input(PWR_EN_12V_PIN)  # store pwr state
    GPIO.output(PWR_EN_12V_PIN, 1)
    GPIO.output([VOL_UP_PIN, VOL_DN_PIN], (GPIO.LOW, GPIO.HIGH))


def hw_vol_stop():
    global _pwr_state
    GPIO.output([VOL_UP_PIN, VOL_DN_PIN], 0)
    GPIO.output(PWR_EN_12V_PIN, _pwr_state)  # restore power state


def get_hw_vol():
    global _t_scan, _update_hw_vol_freq, hw_volume, sw_volume, vol_err, emit_volume, rising_vol
    _t_scan = time.perf_counter()
    vol = int(float(DSP.read_back(_ADD_VOL_READBACK_HIGH, _ADD_VOL_READBACK_LOW)) * 100)
    _activety = GPIO.input(ACTIVITY_PIN)
    # Higher sensitively in turning direction and lower in opposite direction.
    if _activety and rising_vol and (vol > hw_volume or (vol + 1) < hw_volume) or\
            (vol < hw_volume or (vol - 1) > hw_volume):
        _update_hw_vol_freq = 100
        rising_vol = hw_volume < vol
        hw_volume = vol
        log.info("HW Volume: {}%".format(hw_volume))
        vol_err = abs(sw_volume - hw_volume)
        emit_volume = True
    else:
        _update_hw_vol_freq = 1.9
        emit_volume = False
    return hw_volume


def set_hw_vol(vol=None):
    global vol_err
    _TIMEOUT = 0.05
    if vol is None:
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

        # Check if error is decreasing
        if new_vol_err >= vol_err:
            time.sleep(0.75)
            if new_vol_err >= vol_err:
                hw_vol_stop()
                log.err('HW vol error!')
                return False
        vol_err = new_vol_err

        time.sleep(0.005*vol_err)
    hw_vol_stop()
    return False


if __name__ == '__main__':
    while True:
        #vol = round(float(DSP.read_back(_ADD_VOL_READBACK_HIGH, _ADD_VOL_READBACK_LOW) * 100), 2)
        #print(vol)
        time.sleep(0.1)
