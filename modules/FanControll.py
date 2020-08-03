
"""
if pwm channels is not detected try:
Edit: /boot/config.txt.
Add the line: dtoverlay=pwm-2chan
Save the file.
Reboot.
"""


import RPi.GPIO as GPIO
from cfg import *
#import RPIO as GPIO
import pigpio
from modules.pwm import PWM
import time

#pwm = pigpio.pi()
amp_fan = GPIO.PWM(AMPLIFIER_FAN_PIN, 100)
#chassis_fan = GPIO.PWM(CHASSIS_FAN_PIN, 1000)

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup([23, 13, 12, 15, 16], GPIO.OUT)
GPIO.output([15, 16], 0)
#GPIO.setup(AMPLIFIER_FAN_TAC_PIN, GPIO.IN)

def main():
    GPIO.output(23, 1)
    amp_fan.start(98)
    #GPIO.output(AMPLIFIER_FAN_PIN, 1)
    #chassis_fan.start(20)
    #pwm.hardware_PWM(AMPLIFIER_FAN_PIN, 5000, 250000)
    #pwm.hardware_PWM(CHASSIS_FAN_PIN, 5000, 250000)
    #chassi_fan = GPIO.PWM(12, 10)
    #amp_fan = GPIO.PWM(13, 50000)
    #chassi_fan.start(100)
    #amp_fan.start(100)
    #GPIO.output(13, 0)
    #GPIO.output(12, 0)
    while 1:
        #print(GPIO.input(AMPLIFIER_FAN_TAC_PIN))
        time.sleep(0.1)
    #time.sleep(150)
    #chassi_fan.stop()
    #amp_fan.stop()
    #GPIO.output(23,  0)


if __name__ == '__main__':
    try:
        main()
        #pass
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
    #amp_fan.stop()
    print('\nFan Controller Ended.')
