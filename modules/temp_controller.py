#!/usr/bin/env python3
import os, sys, inspect

# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

from modules.shared import *
from threading import Thread
import glob
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([AMPLIFIER_FAN_PIN, CHASSIS_FAN_PIN, PWR_EN_12V_PIN, VOL_UP_PIN, VOL_DN_PIN, AMP_EN_PIN], GPIO.OUT)
GPIO.setup(CHASSIS_FAN_TACH_PIN, GPIO.IN, GPIO.PUD_UP)
amp_fan = GPIO.PWM(AMPLIFIER_FAN_PIN, 1000)  # Setup PWM
chassis_fan = GPIO.PWM(CHASSIS_FAN_PIN, 1000)  # Setup PWM
amp_fan.start(0)
chassis_fan.start(0)
GPIO.setwarnings(True)

# DS18B20 sensor path
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
# RPI CPU temp path
cpu_temp_file = "/sys/class/thermal/thermal_zone0/temp"

# Fan speed controller params
temp_max_amp = 80
temp_max_cpu = 85
temp_min_amp = 55
temp_min_cpu = 25  # 55
update_frequency = 2

# Fan power lower bound cutoff
_amp_fan_lb_threshold = 10
_case_fan_lb_threshold = 5

# Fan rpm data
_amp_fan_rpm_max = AMP_FAN_MAX_RPM
_amp_fan_tach_pin = AMPLIFIER_FAN_TACH_PIN
_case_fan_rpm_max = CHASSIS_FAN_MAX_RPM
_case_fan_tach_pin = CHASSIS_FAN_TACH_PIN

# Temp ctrl params
_Kp_amp = 1
_Kp_case = 1
amp_fan_speed = 0
case_fan_speed = 0
is_alive = False
trd = None

# tach vars
rpm_case = 0
rpm_amp = 0
_tach_amp = _tach_case = 0
_t_last_rpm_read = time.perf_counter()


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
    CPUTemp = float(c.read()) / 1000
    c.close()
    return CPUTemp


def start(verbose=False):
    global trd
    trd = Thread(target=temp_controller_thread, name='TempCtrlThread', args=(verbose,)).start()
    return trd


def stop():
    global is_alive, trd
    if trd is not None and is_alive:
        is_alive = False
        trd.join()
        trd = None
        return True
    return False


def tach_callback(channel):
    global _tach_amp, _tach_case
    if channel == AMPLIFIER_FAN_TACH_PIN:
        _tach_amp += 1
    else:
        _tach_case += 1


# GPIO.add_event_detect(AMPLIFIER_FAN_TACH_PIN, GPIO.FALLING, tach_callback) # todo add when supported by hw
GPIO.add_event_detect(CHASSIS_FAN_TACH_PIN, GPIO.FALLING, tach_callback)


def get_fan_rpm(fan=""):
    """
    Return rpm of fan
    :param fan: select fan
        "amp": Amplifier fan
        "case": case fan
        else : amp and case
    :return: selected fan(s) rpm
    """
    global _t_last_rpm_read, rpm_amp, rpm_case, _tach_amp, _tach_case

    dt = time.perf_counter() - _t_last_rpm_read
    # get rpm by dividing pulses (2/rot) by time delta and multiplying with 30 (60/2) to get pulses minute.
    rpm_amp = 30 * _tach_amp / dt
    rpm_case = 30 * _tach_case / dt
    _tach_case = _tach_amp = 0

    _t_last_rpm_read = time.perf_counter()

    if 'amp' in fan.lower():
        return rpm_amp
    elif 'case' in fan.lower():
        return rpm_case
    else:
        return rpm_amp, rpm_case


def temp_controller_thread(verbose=False):
    global amp_fan_speed, case_fan_speed, is_alive
    GPIO.setmode(GPIO.BCM)
    _t_last_update = time.perf_counter()
    _I_amp = 0
    _I_case = 0
    is_alive = True
    while is_alive:
        # get time delta
        t_now = time.perf_counter()
        dt = t_now - _t_last_update
        _t_last_update = t_now

        # get temp sensor readings
        amp_temp = read_amp_temp()
        cpu_temp = read_cpu_temp()

        # get temp error
        amp_norm_err = np.clip((amp_temp - temp_min_amp) / temp_max_amp, 0.0, 1.0)
        cpu_norm_err = np.clip((cpu_temp - temp_min_cpu) / temp_max_cpu, 0.0, 1.0)
        case_norm_err = max(cpu_norm_err, amp_norm_err)

        # get fan speed
        _amp_fan_speed = np.clip(100 * amp_norm_err * _Kp_amp, 0, 100)
        _case_fan_speed = np.clip(100 * case_norm_err * _Kp_case, 0, 100)

        # set fan speed
        amp_fan_speed = (0, _amp_fan_speed)[float(_amp_fan_speed) > _amp_fan_lb_threshold]
        case_fan_speed = (0, _case_fan_speed)[float(_case_fan_speed) > _case_fan_lb_threshold]

        if amp_fan_speed or case_fan_speed:
            pwr12v.set()
            if get_fan_rpm('case') < 10:
                case_fan_speed = 100
        elif _amp_fan_speed < _amp_fan_lb_threshold - 5 and _case_fan_speed < _case_fan_lb_threshold - 5:
            pwr12v.release()

        amp_fan.ChangeDutyCycle(amp_fan_speed)
        chassis_fan.ChangeDutyCycle(case_fan_speed)

        if verbose:
            disp_temp(amp_temp, cpu_temp)

        t_sleep = max(1 / update_frequency - dt, 0.1)
        time.sleep(t_sleep)
    pwr12v.release()


def disp_temp(t_amp=None, t_cpu=None):
    if t_amp is None:
        t_amp = read_amp_temp()
    if t_cpu is None:
        t_cpu = read_cpu_temp()

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    log.info('\n\tTime: {}\n'
             '\tCPU temp: {}\n'
             '\tAMP temp: {}\n'
             '\tCaseFan power: {}\n'
             '\tAmpFan power: {}'.format(timestamp,
                                         t_cpu,
                                         t_amp,
                                         round(case_fan_speed),
                                         round(amp_fan_speed)))


def temp_ctrl_test():
    start()
    while True:
        disp_temp()
        print('\tCase RPM:' + str(get_fan_rpm('case')))
        time.sleep(2)


if __name__ == '__main__':
    try:
        log.set_level(LOGLEVEL.INFO)
        pwr12v.verbose = True
        temp_ctrl_test()

    except KeyboardInterrupt:
        is_alive = False
        print('\nTemp read stopped')
