import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from threading import get_ident
from cfg import *


class POWER12V:
    GPIO.setmode(GPIO.BCM)

    def __init__(self):
        self._client_list = []

    def on(self):
        ident = get_ident()
        new_req = False
        if ident not in self._client_list:
            self._client_list.append(ident)
            new_req = True
        GPIO.output(PWR_EN_12V_PIN, GPIO.HIGH)
        return new_req

    def off(self):
        ident = get_ident()
        if ident not in self._client_list:
            log.warn('Power was not set from this thread!\nUse POWER12V to enable power.')
        else:
            self._client_list.pop(ident)
        if not self._client_list:
            GPIO.output(PWR_EN_12V_PIN, GPIO.LOW)

    def get_clients(self):
        return self._client_list

    def clear_client(self, ident=None):
        if ident is None:
            ident = get_ident()
        ret = False

        if ident in self._client_list:
            self._client_list.pop(ident)
            ret = True

        return ret

    def clear_clients(self):
        if not self._client_list:
            return False
        self._client_list = []
        return True
