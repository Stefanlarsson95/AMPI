import wiringpi
from time import sleep

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(27, wiringpi.OUTPUT)
wiringpi.pinMode(18, 2)  # hardware pwm only works on GPIO port 18
wiringpi.pwmWrite(18, 0)  # duty cycle between 0 and 1024
# 0 = off and 1024 = constantly on

pause_time = 0.002  # you can change this to slow down/speed up

try:
    print('starting')
    while True:
        for i in range(0, 1025):  # 1025 because it stops at 1024
            wiringpi.pwmWrite(18, i)
            sleep(pause_time)
        for i in range(1024, -1, -1):  # from 1024 to zero in steps of -1
            wiringpi.pwmWrite(13, i)
            sleep(pause_time)

finally:
    print('stopping')
    wiringpi.pwmWrite(13, 0)  # switch PWM output to 0
    wiringpi.pinMode(13, 0)  # GPIO18 to input
    wiringpi.pinMode(27, 0)