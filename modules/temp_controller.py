#!/usr/bin/env python3
from cfg import *
from threading import Thread
import glob
import time
import numpy as np

# DS18B20 sensor path
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
# RPI CPU temp path
cpu_temp_file = "/sys/class/thermal/thermal_zone0/temp"

# Fan speed controller params
temp_target_amp = 20  # AMP_TEMP_TARGET
temp_target_cpu = 20  # CPU_TEMP_TARGET
update_interval = 1

_amp_fan_rpm_max = AMP_FAN_MAX_RPM
_amp_fan_tach_pin = AMPLIFIER_FAN_TACH_PIN
_case_fan_rpm_max = CHASSIS_FAN_MAX_RPM
_case_fan_tach_pin = CHASSIS_FAN_TACH_PIN

# Temp PI params
_Kp_amp = 1
_Ki_amp = 0.1
_I_amp_lim = 75
_Kp_case = 1
_Ki_case = 0.1
_I_case_lim = 75

# Fan PI params
_Kp_fan_amp = 100
_Ki_fan_amp = 0.1
_Kp_fan_case = 100
_Ki_fan_case = 0.1

amp_fan_speed = -1
case_fan_speed = -1
amp_fan_rpm = -1
case_fan_rpm = -1
amp_fan_pwr = -1
case_fan_pwr = -1
amp_rpm_true = -1
case_rpm_true = -1
amp_tach = 0
case_tach = 0


def read_amp_temp():
    """
    Read value of DS18B20 amplifier temp sensor
    :return: Amplifier heat sink temperature
    """

    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


def read_cpu_temp():
    """
    Read RPi cpu temperature
    :return: RPi cpu temperature
    """
    c = open(cpu_temp_file)
    CPUTemp = int(c.read()) / 1000
    c.close()
    return CPUTemp


def init_temp_controller():
    trd = Thread(target=temp_controller_thread, name='TempCtrlThread', )
    trd.daemon = False  # True
    trd.start()
    return trd


def tach_callback(channel):
    global amp_tach, case_tach
    if channel == _amp_fan_tach_pin:
        amp_tach += 1
    elif channel == _case_fan_tach_pin:
        case_tach += 1
    else:
        log.warn('Unsupported tach channel')


def _fan_controller_thread():
    global amp_fan_rpm, case_fan_rpm, amp_tach, case_tach, amp_fan_pwr, case_fan_pwr, amp_rpm_true, case_rpm_true
    _t_last_update = time.perf_counter()
    _I_amp_fan = 0
    _I_case_fan = 0
    GPIO.setup(_case_fan_tach_pin, GPIO.IN, GPIO.PUD_UP)  # fixme wrong pin?
    GPIO.add_event_detect(_amp_fan_tach_pin, GPIO.RISING, tach_callback, bouncetime=5)
    GPIO.add_event_detect(_case_fan_tach_pin, GPIO.RISING, tach_callback, bouncetime=2)
    amp_fan.ChangeDutyCycle(100)

    while True:
        # get time delta
        t_now = time.perf_counter()
        dt = t_now - _t_last_update
        _t_last_update = t_now
        sf = np.clip(dt, 0.01, 0.1)

        # set fan rpm proportional to speed
        amp_fan_rpm = _amp_fan_rpm_max * amp_fan_speed / 100
        case_fan_rpm = _case_fan_rpm_max * case_fan_speed / 100

        amp_rpm_true = 15 * amp_tach / dt
        amp_tach = 0
        _case_rpm_true = 15 * case_tach / dt
        case_rpm_true = case_rpm_true * 0.99 + _case_rpm_true * 0.01
        case_tach = 0

        # get fan rpm error
        err_amp = amp_fan_rpm - amp_rpm_true
        err_case = case_fan_rpm - case_rpm_true

        _I_amp_fan += err_amp * dt * 0.01
        _I_amp_fan = np.clip(_I_amp_fan, 0, 10)
        _I_case_fan += err_amp * dt * 0.01
        _I_case_fan = np.clip(_I_case_fan, -100, 100)

        _amp_fan_pwr = err_amp * 0.01 + _I_amp_fan * 100
        amp_fan_pwr = np.clip(amp_fan_pwr * 0.99 + _amp_fan_pwr * 0.01, 0, 100)
        # amp_fan_pwr = (10, amp_fan_pwr)[amp_fan_pwr > 10]
        case_fan_pwr = np.clip(err_case * 0.1 + _I_case_fan, 0, 100)
        # print(amp_fan_pwr)
        # print(err_amp)
        print(str(amp_rpm_true))
        #print(sf)

        #amp_fan.ChangeDutyCycle(100)
        # amp_fan.ChangeDutyCycle(amp_fan_pwr)
        _temp_pwr = 100 * case_fan_rpm / _case_fan_rpm_max
        # chassis_fan.ChangeDutyCycle(case_fan_pwr)
        # chassis_fan.ChangeDutyCycle(_temp_pwr)

        # err_t = max(err_amp, err_case)
        err_t = abs(err_amp)
        t_sleep = float(np.clip(1 - err_t / 100, 0.1, 1))
        time.sleep(t_sleep)


def temp_controller_thread():
    global amp_fan_rpm, case_fan_rpm, amp_fan_speed, case_fan_speed
    GPIO.setmode(GPIO.BCM)
    _t_last_update = time.perf_counter()
    _I_amp = 0
    _I_case = 0

    t = Thread(target=_fan_controller_thread)
    t.daemon = True
    t.start()
    while True:
        # get time delta
        t_now = time.perf_counter()
        dt = t_now - _t_last_update
        _t_last_update = t_now

        # get temp sensor readings
        amp_temp = read_amp_temp()
        cpu_temp = read_cpu_temp()

        # get temp error
        amp_temp_err = amp_temp - temp_target_amp
        case_temp_err = max(cpu_temp - temp_target_cpu, amp_temp_err)

        # error integration
        _I_amp += amp_temp_err * _Ki_amp * dt
        _I_amp = (_I_amp, _I_amp_lim)[_I_amp > _I_amp_lim]
        _I_case += case_temp_err * _Ki_case * dt
        _I_case = (_I_case, _I_case_lim)[_I_case > _I_case_lim]

        # get fan speed
        amp_fan_speed = np.clip(amp_temp_err * _Kp_amp + _I_amp, 0, 100)
        case_fan_speed = np.clip(case_temp_err * _Kp_case + _I_case, 0, 100)

        t_sleep = max(1 / update_interval - dt, 0.1)
        time.sleep(t_sleep)


class TempController:
    def __init__(self, on_lim, fan_max_speed, fan_temp_read, fan_pwm_obj, tach_pin=None):
        self.temp = -1
        self.fan_speed = 0
        self.update_interval = 1
        self.isAlive = False

        self._temp_target = on_lim
        self._hysteres = on_lim - 5
        self._fan_temp_read = fan_temp_read
        self._Kp = 20
        self._Ki = 0.01
        self._fan_obj = fan_pwm_obj
        self._fan_tach = 0
        self._tach_pin = tach_pin
        self._max_speed = fan_max_speed

    def temp_read(self):
        """
        Get temp reading
        :return: Temperature reading
        """
        temp = self._fan_temp_read()
        self.temp = temp
        return temp

    def set_temp_lim(self, lim):
        if 0 < lim < 120:
            self._temp_target = lim
            return True
        log.warn('Unsupported temp limit. Must be within [0 < 120]')
        return False

    def start(self):
        t = Thread(name='TempCtrlThread', target=self.temp_controller(), )
        t.daemon = True
        t.start()
        if self._tach_pin:
            GPIO.add_event_callback(self._tach_pin, self._fan_callback)
        return self

    def stop(self):
        self.isAlive = False

    def temp_controller(self):
        GPIO.setmode(GPIO.BCM)
        _t_last_update = 0
        self.isAlive = True
        if self._tach_pin:
            Thread(target=self._fan_controller).start()
        while self.isAlive and self.update_interval > 0:

            t_now = time.perf_counter()
            dt = t_now - _t_last_update
            _t_last_update = t_now

            temp = self.temp_read()

            temp_err = temp - self._temp_target

            fan_speed = temp_err * self._Kp

            if self._tach_pin is None:
                self._fan_obj.ChangeDutyCycle(fan_speed)

            self.temp = temp

            time.sleep(max(1 / self.update_interval - dt, 0.1))

    def _fan_controller(self):
        _t_last = 0
        _I = 0
        _Kp = 10
        _Ki = 0.01
        while self.isAlive:
            t_now = time.perf_counter()
            dt = t_now - _t_last
            _t_last = t_now

            rpm_req = self._max_speed * self.fan_speed / 100
            rpm_true = self._fan_tach / dt
            self._fan_tach = 0

            err = rpm_req - rpm_true
            _I += err * dt

            pwr = err * _Kp + _I * _Ki

            self._fan_obj.ChangeDutyCycle(pwr)

            time.sleep(max(1 - dt, 0.1))

    def _fan_callback(self, channel):
        self._fan_tach += 1


def fan_speed_test(speed):
    global amp_fan_speed, case_fan_speed
    GPIO.output(PWR_EN_12V_PIN, 1)
    Thread(target=_fan_controller_thread).start()
    amp_fan_speed = speed
    case_fan_speed = speed

    while True:
        time.sleep(1)

    while True:
        amp_temp = read_amp_temp()
        print('CpuTemp: ' + str(read_cpu_temp()))
        print('AmpTemp: ' + str(amp_temp))
        print('AmpFanRpm: ' + str(round(amp_rpm_true)))
        print('CaseFanRpm: ' + str(round(case_rpm_true)))
        time.sleep(1)


def temp_ctrl_test(temp, sensor='both'):
    global temp_target_amp, temp_target_cpu
    if sensor == 'cpu':
        temp_target_cpu = temp
    elif sensor == 'amp':
        temp_target_amp = temp
    elif sensor == 'boot':
        temp_target_amp = temp_target_cpu = temp
    else:
        log.warn('Unsupported sensor')

    ctrl_thread = init_temp_controller()
    while True:
        print('CpuTemp: ' + str(read_cpu_temp()))
        print('AmpTemp: ' + str(read_amp_temp()))
        print('CaseFanPwr: ' + str(case_fan_pwr))
        time.sleep(1)


if __name__ == '__main__':

    try:
        # temp_ctrl_test(temp=25)
        fan_speed_test(speed=50)

    except KeyboardInterrupt:
        GPIO.cleanup()
        print('\nTemp read stopped')
