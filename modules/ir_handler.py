from cfg import IR_PIN, log
from IR.IRModule import IRRemote
from multiprocessing import Process, Event, Queue
from threading import Thread, Lock
import RPi.GPIO as GPIO
import numpy as np

key_mapping = {2011249184: 'enter',
               2011254816: 'up',
               2011246624: 'down',
               2011271200: 'left',
               2011258912: 'right',
               2011283488: 'menu',
               2011298336: 'play_pause',
               0: 'hold'}


def print_key(key_id):
    print(str(key_id) + ' : ' + key_mapping.get(key_id, 'No mapping'))


class IR:
    def __init__(self, pin, func_key=None, key_names=None, verbose=False):
        # key function vars

        self.functions = {}
        self.key_names = key_names if key_names is not None else {}

        # Event handle vars
        self.is_alive = False
        self.shutdown_event = Event()
        self.ir_event = Event()
        self.ir_queue = Queue()
        self.ir_queue_lock = Lock()

        self.ir_thread = Thread(name='ir_event_thread', target=self.ir_event_handler)
        self.ir_process = Process(name='ir_listener_process',
                                  target=self.ir_event_listener,
                                  args=(pin,
                                        self.ir_event,
                                        self.shutdown_event,))

    def start(self):
        if not self.is_alive:
            self.is_alive = True
            self.ir_process.start()
            self.ir_thread.start()

        return self

    def stop(self):
        if self.is_alive:
            self.shutdown_event.set()
            while not self.ir_queue.empty():
                self.ir_queue.get()
            self.ir_thread.join()

    def add_key(self, key_id, function, name=None):
        if name is None:
            name = self.key_names.get(key_id, str(key_id))
        self.functions[key_id] = [function, name]

    def match_key_id(self, key_id, tol=0.5):
        if key_id in self.functions.keys():
            return key_id

        best = tol
        ret = -1

        for v, _ in self.functions.items():
            diff = bin(v ^ key_id)
            diff_avg = diff.count("1") / len(diff)
            if diff_avg < best:
                best = diff_avg
                ret = v

        return ret

    # ## Thread functions ###

    def ir_event_handler(self):
        """
        Event handler.
        Cal functions from self.functions['func_key']
        where func_key is a defined function corresponding to a pressed key.
        :return:
        """
        while self.is_alive and not self.shutdown_event.is_set():
            assert self.is_alive, "Ir handler not started! Call IR.start()"
            key_events = []

            self.ir_event.wait()  # wait for new queue

            while not self.ir_queue.empty():
                key = self.ir_queue.get()
                key_events.append(key)

            self.ir_event.clear()  # indicate done with queue read

            for key in key_events:
                key_matched = self.match_key_id(key_id=key, tol=1)
                if key_matched != -1:
                    self.functions[key_matched][0](key_matched)  # call key function
                else:
                    log.warn('Key [{}] have no defined function!\nMapped keys:'.format(key))
                    for _, v in self.functions.items():
                        print('{}() ~ {}'.format(v[0].__name__, v[1]))

    # ### Process functions ###

    def ir_event_callback(self, key):
        self.ir_queue.put(key)
        self.ir_event.set()

    def ir_event_listener(self, pin, ir_event, shutdown_event):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)  # set pin IR_PIN to input
        remote = IRRemote(self.ir_event_callback)  # initiate IR remote
        remote.checkTime = 50
        self.ir_event = ir_event  # sync ir event # todo check if necessary
        while not shutdown_event.is_set() and GPIO.getmode() == GPIO.BCM:
            ret = GPIO.wait_for_edge(pin, GPIO.BOTH, timeout=1000)  # blocking wait for edge
            if ret is not None:
                remote.pWidth(ret)  # check pin activity


if __name__ == '__main__':
    ir_handler = IR(IR_PIN).start()

    for key in key_mapping:
        ir_handler.add_key(key, print_key, key_mapping[key])
    try:
        ir_handler.ir_thread.join()
    except KeyboardInterrupt:
        pass
    ir_handler.stop()
