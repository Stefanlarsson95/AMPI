import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([23, 13, 12, 15, 16], GPIO.OUT)
GPIO.setup([7], GPIO.IN)
GPIO.output([15, 16], 0)
GPIO.output(23, 0)

_t_switch = time.perf_counter()
_spdif_lock = False
_debounce = 0.1

print('S/PDIF enabled')
try:
    while True:
        optical_lock = not GPIO.input(7)
        if optical_lock != _spdif_lock and time.perf_counter() - _t_switch > _debounce:
            _t_switch = time.perf_counter()
            _spdif_lock = not _spdif_lock
            print('Optical lock: ' + ('False', 'True')[_spdif_lock])
            GPIO.output(23, _spdif_lock)
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

GPIO.output(23, 0)

print('\nS/PDIF disabled')

