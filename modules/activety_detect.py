import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

GPIO.setup(0, GPIO.IN)

TIME = datetime.datetime.now().strftime("%H:%M:%S")
print('Initialized: ' + str(TIME))
t_now = time.time()

while True:
    state = GPIO.input(0)
    if state and time.time() - t_now > 0.1:
        t_now = time.time()

        TIME = datetime.datetime.now().strftime("%H:%M:%S")
        print('Activity at: ' + str(TIME))
    time.sleep(0.01)
