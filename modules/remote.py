from cfg import *
import RPi.GPIO as GPIO
import IR.IRModule as IRModule
import time


class IRRemote(IRModule.IRRemote):
    ir_code = {
        0x77e15020: "up",
        0x77e13020: "down",
        0x77e16020: "right",
        0x77e19020: "left",
        0x77e13a20: "enter",
        0x77e1c020: "menu",
        0x77e1fa20: "pp",
        0x00000000: "hold"
    }

    def __init__(self, ir_event_callback):
        self.sensor_pin = IR_PIN
        self.ir_event_callback = ir_event_callback
        self.remote = super().__init__(callback=self._ir_event_callback)

    def _ir_event_callback(self, code):
        """
        Interprets ir code and calls external ir event callback with interpret code as argument
        :param code: ir hex code
        :return: None
        """
        key = IRRemote.ir_code.get(code, -1)
        if self.verbose:
            print(str(key))
        self.ir_event_callback(key)


def main():
    def print_key(key):
        print(key)

    remote = IRRemote(print_key)

    while True:
        time.sleep(10000)


if __name__ == '__main__':
    main()
