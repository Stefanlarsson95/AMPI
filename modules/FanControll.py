import RPi.GPIO as GPIO
#from modules import logger
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#log = logger.Log()
GPIO.setup([23, 13,12, 15, 16], GPIO.OUT)
GPIO.output([15,16], 0)


def main():
    GPIO.output(23,1)
    chassi_fan = GPIO.PWM(12, 10)
    amp_fan = GPIO.PWM(13, 50000)
    chassi_fan.start(100)
    amp_fan.start(100)
    while 1:
        pass
    #time.sleep(150)
    #chassi_fan.stop()
    #amp_fan.stop()
    #GPIO.output(23,  0)




if __name__ == '__main__':
    time.sleep(1)
    main()