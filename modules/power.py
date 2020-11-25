"""
12V power enable functions.
Used when multiple clients are requesting to use the power enable pin.
The class will initiate a client list of all threads requesting a ON state.
This will activate the 12v power. A client can the request a OFF state and thus be removed from the client list.
When the last client is removed from the list the power will be disabled.
"""

import os, sys, inspect

# = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

from cfg import *
from threading import get_ident, Lock


class POWER12V:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PWR_EN_12V_PIN, GPIO.OUT, initial=GPIO.LOW)

    def __init__(self, init_on=False, verbose=False):
        self._client_list = []
        self._action_lock = Lock()
        self.verbose = verbose
        if init_on:
            self.on()

    def on(self):
        """
        Add calling thread to client list and enable 12v power.
        :return: True if power was turned on, False if already on.
        """
        ident = get_ident()
        pwr_new = False
        with self._action_lock:
            if ident not in self._client_list:
                self._client_list.append(ident)
            if not GPIO.input(PWR_EN_12V_PIN):
                GPIO.output(PWR_EN_12V_PIN, GPIO.HIGH)
                pwr_new = True
        if self.verbose and pwr_new:
            log.info('12V power activated by: ' + str(ident))
        return pwr_new

    def off(self):
        """
        Remove calling thread if in client list. Will deactivate 12v power if client list is empty.
        :return: True if power was disabled, else False
        """
        ident = get_ident()
        with self._action_lock:
            if not GPIO.input(PWR_EN_12V_PIN):
                return False
            if ident not in self._client_list:
                log.warn('Power was never set from this thread!\nUse POWER12V.on() to enable power.')
            else:
                self._client_list.remove(ident)
            if not self._client_list:
                GPIO.output(PWR_EN_12V_PIN, GPIO.LOW)
                if self.verbose:
                    log.info('12V power deactivated by: ' + str(ident))
                return True

    def get_clients(self):
        with self._action_lock:
            return self._client_list

    def clear_client(self, ident=None):
        if ident is None:
            ident = get_ident()
        ret = False
        with self._action_lock:
            if ident in self._client_list:
                self._client_list.pop(ident)
                ret = True

        return ret

    def clear_clients(self):
        with self._action_lock:
            if not self._client_list:
                return False
            self._client_list = []
        return True
