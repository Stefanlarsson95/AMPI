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
temp_target_amp = AMP_TEMP_TARGET
temp_target_cpu = CPU_TEMP_TARGET
update_interval = 2

_amp_fan_rpm_max = AMP_FAN_MAX_RPM
_amp_fan_tach_pin = AMPLIFIER_FAN_TACH_PIN
_case_fan_rpm_max = CHASSIS_FAN_MAX_RPM
_case_fan_tach_pin = CHASSIS_FAN_TACH_PIN

# Temp PI params
_Kp_amp = 3
_Ki_amp = 10e-3
_I_amp_lim = 65
_Kp_case = 5
_Ki_case = 10e-3
_I_case_lim = 65

amp_fan_speed = 0
case_fan_speed = 0

amp_fan_lb_threshold = 50
case_fan_lb_threshold = 35

is_alive = False


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
    trd = Thread(target=temp_controller_thread, name='TempCtrlThread').start()
    return trd


def temp_controller_thread():
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
        amp_temp_err = amp_temp - temp_target_amp
        case_temp_err = max(cpu_temp - temp_target_cpu, amp_temp_err)

        # error integration
        _I_amp += amp_temp_err * _Ki_amp * dt
        _I_amp = np.clip(_I_amp, 0, _I_amp_lim)
        _I_case += case_temp_err * _Ki_case * dt
        _I_case = np.clip(_I_case, 0, _I_case_lim)

        # get fan speed
        _amp_fan_speed = np.clip(amp_temp_err * _Kp_amp + _I_amp, 0, 100)
        amp_fan_speed = (0, _amp_fan_speed)[float(_amp_fan_speed) > amp_fan_lb_threshold]
        _case_fan_speed = np.clip(case_temp_err * _Kp_case + _I_case, 0, 100)
        case_fan_speed = (0, _case_fan_speed)[float(_case_fan_speed) > case_fan_lb_threshold]

        if amp_fan_speed or case_fan_speed:
            pwr12v.on()
        elif _amp_fan_speed < amp_fan_lb_threshold - 5 and _case_fan_speed < case_fan_lb_threshold - 5:
            pwr12v.off()

        amp_fan.ChangeDutyCycle(amp_fan_speed)
        chassis_fan.ChangeDutyCycle(case_fan_speed)

        t_sleep = max(1 / update_interval - dt, 0.1)
        time.sleep(t_sleep)
    pwr12v.off()


def temp_ctrl_test(temp, sensor='both'):
    global temp_target_amp, temp_target_cpu
    if sensor == 'cpu':
        temp_target_cpu = temp
    elif sensor == 'amp':
        temp_target_amp = temp
    elif sensor == 'both':
        temp_target_amp = temp_target_cpu = temp
    else:
        log.warn('Unsupported sensor')
    init_temp_controller()
    import datetime
    #import csv
    #f = open('temperature_data.csv', 'w')
    #writer = csv.writer(f)
    #row = {'Time', 'Cpu Temp', 'Amp Temp', 'Case Fan Speed', 'Amp Fan Speed'}
    #writer.writerow(row)
    while True:
        amp_temp = read_amp_temp()
        cpu_temp = read_cpu_temp()
        t = datetime.datetime.now().strftime("%H:%M:%S")
        print('Time: ' + t)
        print('CpuTemp: ' + str(cpu_temp))
        print('AmpTemp: ' + str(amp_temp))
        print('CaseFanPwr: ' + str(round(case_fan_speed)))
        print('AmpFanPwr: ' + str(round(amp_fan_speed)))
        #row = [t, cpu_temp, amp_temp, case_fan_speed, amp_fan_speed]
        #writer.writerow(row)
        time.sleep(10)


if __name__ == '__main__':
    try:
        GPIO.output(AMP_EN_PIN, 0)
        log.set_level(LOGLEVEL.INFO)
        pwr12v.verbose = True
        temp_ctrl_test(60)

    except KeyboardInterrupt:
        is_alive = False
        print('\nTemp read stopped')
