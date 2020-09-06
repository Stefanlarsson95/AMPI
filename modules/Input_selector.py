from cfg import *
from hardware import adau1701 as DSP
import time
from threading import Thread

# Split register in high and low byte
_AUX_DETECT_REG = divmod(AUX_DETECT_REG, 0x100)
_RPI_DETECT_REG = divmod(RPI_DETECT_REG, 0x100)
_SPDIF_DETECT_REG = divmod(SPDIF_DETECT_REG, 0x100)


class InputSelector:
    def __init__(self, init_source='auto', signal_timeout=30):
        self.source = init_source
        self.signal_timeout = signal_timeout
        self._any_signal = False
        self._t_first_signal = 0
        self._t_last_signal = 0
        self._t_active = 0
        self._t_debounce = 0.1
        self.spdif_enabled = False
        self.aux_detected = 0
        self.rpi_detected = 0
        self.spdif_detected = 0
        self._amp_pin = AMPLIFIER_ENABLE_PIN
        self._spdif_pin = SPDIF_LOCK_PIN
        self.amp_always_on = False
        self.amp_en = self.amp_always_on
        self._is_running = False

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True
        self._is_running = True
        t.start()
        return self

    def run(self):
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self._amp_pin, GPIO.OUT)
        GPIO.setup(self._spdif_pin, GPIO.IN, GPIO.PUD_UP)
        #GPIO.setup(23, GPIO.OUT)
        #GPIO.output(23, 0)

        while self._is_running:
            spdif_lock = not GPIO.input(self._spdif_pin)  # inverted

            _aux = DSP.read_back(_AUX_DETECT_REG[0], _AUX_DETECT_REG[1])
            _rpi = DSP.read_back(_RPI_DETECT_REG[0], _RPI_DETECT_REG[1])

            EN_12V = not _aux and not _rpi and spdif_lock
            GPIO.output(23, EN_12V)  # activate 12v if spdif lock. fixme temporary

            _spdif = DSP.read_back(_SPDIF_DETECT_REG[0], _SPDIF_DETECT_REG[1]) and spdif_lock

            if _aux or _rpi or _spdif:
                if not self._any_signal:
                    self._any_signal = True
                    self._t_first_signal = time.perf_counter()
                self._t_last_signal = time.perf_counter()
                t_active = self._t_last_signal - self._t_first_signal
                if t_active > self._t_debounce or self.amp_always_on:
                    self.amp_en = True
            else:
                self._any_signal = False
                t_active = 0
                if time.perf_counter() > self._t_last_signal + self.signal_timeout and not self.amp_always_on:
                    self.amp_en = False

            GPIO.output(self._amp_pin, self.amp_en)
            self.aux_detected = _aux
            self.rpi_detected = _rpi
            self.spdif_detected = _spdif

            time.sleep(1)

    def stop(self):
        self._is_running = False


if __name__ == '__main__':

    input_select = InputSelector().start()
    try:
        while True:
            aux = input_select.aux_detected
            rpi = input_select.rpi_detected
            spdif = input_select.spdif_detected
            amp_on = input_select.amp_en

            print('AUX: {}\nRPI: {}\nSPDIF: {}\nAMP enabled: {}'.format(aux, rpi, spdif, amp_on))
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(PWR_EN_12V_PIN, 0)
