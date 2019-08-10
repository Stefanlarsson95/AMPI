#!/usr/bin/python
import time
from multiprocessing import Process as mp #import Process,Value,Array ,Manager,Lock;
from threading import Thread
from modules import OLED
from modules import logger, volume as vol
import math
log = logger.Log(logger.LOGLEVEL.INFO)
tInit = time.time()


def initializer():
    VolumeHandeler = Thread(target=vol.update_volume(), name='VolumeHandler')
    OledHandler = Thread(target=OLED.main_process, name='OledHandler')
    VolumeHandeler.start()
    OledHandler.start()

def main():
    initializer()
    while True:
        print("vol:" + str(vol.hw_volume))
        time.sleep(0.5)

if __name__ == '__main__':
    main()
