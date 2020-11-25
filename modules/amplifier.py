"""
Amplifier control module
Used to start and shutdown amplifier
"""
from cfg import *
from threading import get_ident, Lock


class AMPLIFIER:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(AMP_EN_PIN, GPIO.OUT, initial=GPIO.LOW)

    def __init__(self, verbose=False):
        self._client_list = []
        self._action_lock = Lock()
        self.verbose = verbose

    def on(self):
        """
        Activate amplifier and add caller to client list
        :return: True if amplifier was turned on. False if already activated.
        """
        ident = get_ident()

        new_act = False
        with self._action_lock:

            if ident not in self._client_list:
                self._client_list.append(ident)
            if not GPIO.input(AMP_EN_PIN):
                GPIO.output(AMP_EN_PIN, GPIO.HIGH)
                new_act = True
        if self.verbose and new_act:
            log.info('Amplifier activated by: ' + str(ident))
        return new_act

    def off(self):
        """
        Remove caller from client list. Amplifier will be shut down if no clients requiring amplifier.
        :return: True if shut down, else False.
        """
        ident = get_ident()

        with self._action_lock:
            if ident not in self._client_list:
                log.warn('Amplifier was never activated by this thread!\nUse AMPLIFIER.on() to activate amplifier.')
            else:
                idx = self._client_list.index(ident)
                self._client_list.remove(idx)

            if not self._client_list:
                GPIO.output(AMP_EN_PIN, GPIO.LOW)
                if self.verbose:
                    log.info('Amplifier was shut down by: ' + str(ident))
                return True
        return False

    def get_clients(self):
        with self._action_lock:
            return self._client_list
