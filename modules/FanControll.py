import RPi.GPIO as GPIO
#import RPIO as GPIO
from pwm import PWM
#from modules import logger
import time

amp_fan_pwm = PWM(0)
chassis_fan_pwm = PWM(1)
amp_fan_pwm.export()
chassis_fan_pwm.export()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([23, 13,12, 15, 16], GPIO.OUT)
GPIO.output([15, 16], 0)


def main():
    GPIO.output(23, 1)
    amp_fan_pwm.duty_cycle = 250000
    amp_fan_pwm.period = 1000000
    amp_fan_pwm.enable = True
    #chassi_fan = GPIO.PWM(12, 10)
    #amp_fan = GPIO.PWM(13, 50000)
    #chassi_fan.start(100)
    #amp_fan.start(100)
    while 1:
        pass
    #time.sleep(150)
    #chassi_fan.stop()
    #amp_fan.stop()
    #GPIO.output(23,  0)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
    amp_fan_pwm.enable = False
    amp_fan_pwm.unexport()
    print('\nFan Controller Ended.')
