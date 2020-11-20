from cfg import *
from hardware import adau1701 as DSP
import time
from threading import Thread

# Split register in high and low byte
_AUX_DETECT_REG = divmod(AUX_DETECT_REG, 0x100)
_RPI_DETECT_REG = divmod(RPI_DETECT_REG, 0x100)
_SPDIF_DETECT_REG = divmod(SPDIF_DETECT_REG, 0x100)
_DSP_SOURCE_SELECT = divmod(DSP_SOURCE_SELECT, 0x100)


class InputSelector:
    def __init__(self, init_source=SOURCE_AUTO, signal_timeout=30):
        self.source = init_source
        self.spdif_lock = False
        self.signal_timeout = signal_timeout
        self.spdif_enabled = False
        self.aux_detected = 0
        self.rpi_detected = 0
        self.spdif_detected = 0
        self.amp_always_on = False
        self.amp_en = self.amp_always_on
        self._any_signal = False
        self._dsp_source = 3  # self.get_dsp_source()
        self._t_first_signal = 0
        self._t_last_signal = 0
        self._t_active = 0
        self._t_debounce = 0.1
        self._amp_pin = AMPLIFIER_ENABLE_PIN
        self._spdif_pin = SPDIF_LOCK_PIN
        self.is_alive = False

        GPIO.output(self._amp_pin, self.amp_en)

    def start(self):
        t = Thread(target=self.run)
        t.start()
        return self

    def run(self):
        global emit_shutdown
        _rpi = _spdif = _aux = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._spdif_pin, GPIO.IN, GPIO.PUD_UP)
        self.is_alive = True
        while self.is_alive and not emit_shutdown:

            # get state of SPDIF lock
            spdif_lock = not GPIO.input(self._spdif_pin)  # inverted

            # Check for source change
            if self._dsp_source != self.source:
                pass
                # self.set_dsp_source(self.source)
            if self.source == SOURCE_AUTO:
                en_spdif = not _aux and not _rpi and _spdif
            elif self.source == SOURCE_SPDIF:
                en_spdif = _spdif

            # GPIO.output(PWR_EN_12V_PIN, self.spdif_lock)  # activate 12v if spdif lock. fixme temporary
            GPIO.output(SPDIF_ENABLE_PIN, spdif_lock)  # activate spdif relay if spdif lock. fixme temporary

            # check for spdif lock state change
            if self.spdif_lock != spdif_lock:
                with i2c_lock:
                    self.dsp_reset(0.5)  # reset dsp
                self.spdif_lock = spdif_lock

            # get source status
            with i2c_lock:
                _aux = bool(DSP.read_back(_AUX_DETECT_REG[0], _AUX_DETECT_REG[1]))
                _rpi = bool(DSP.read_back(_RPI_DETECT_REG[0], _RPI_DETECT_REG[1]))
                _spdif = self.spdif_lock and bool(DSP.read_back(_SPDIF_DETECT_REG[0], _SPDIF_DETECT_REG[1]))

            # amp enable
            if not AMP_ALWAYS_OFF and (_aux or _rpi or _spdif):
                if not self._any_signal:
                    self._any_signal = True
                    self._t_first_signal = time.perf_counter()
                self._t_last_signal = time.perf_counter()
                t_active = self._t_last_signal - self._t_first_signal
                if t_active > self._t_debounce or self.amp_always_on:
                    self.amp_en = True
            else:
                self._any_signal = False
                if time.perf_counter() > self._t_last_signal + self.signal_timeout and not self.amp_always_on:
                    self.amp_en = False
            GPIO.output(self._amp_pin, self.amp_en)

            self.aux_detected = bool(_aux)
            self.rpi_detected = bool(_rpi)
            self.spdif_detected = bool(_spdif)

            t_sleep = (0.1, 1)[standby]
            time.sleep(t_sleep)

    def stop(self):
        self.is_alive = False

    def set_dsp_source(self, dsp_source):
        if dsp_source not in [SOURCE_AUTO, SOURCE_AUX, SOURCE_RPI, SOURCE_SPDIF]:
            log.err('Unsupported source')
            return -1
        with i2c_lock:
            DSP.write_param(DSP_SOURCE_SELECT, dsp_source)
            time.sleep(0.1)
            _source = DSP.read_back(_DSP_SOURCE_SELECT[0], _DSP_SOURCE_SELECT[0])
            self._dsp_source = _source
            return _source

    def get_dsp_source(self):
        with i2c_lock:
            _source = DSP.read_back(_DSP_SOURCE_SELECT[0], _DSP_SOURCE_SELECT[0])
        self._dsp_source = _source
        return _source

    @staticmethod
    def dsp_reset(t_sleep=1.0):
        GPIO.setup(DSP_RST_PIN, GPIO.OUT)
        GPIO.output(DSP_RST_PIN, 0)
        time.sleep(t_sleep)
        GPIO.setup(DSP_RST_PIN, GPIO.IN)


if __name__ == '__main__':

    input_select = InputSelector().start()
    try:
        while True:
            aux = input_select.aux_detected
            rpi = input_select.rpi_detected
            spdif = input_select.spdif_detected
            amp_on = input_select.amp_en
            amp_rst = GPIO.input(DSP_RST_PIN)

            print('AUX: {}\nRPI: {}\nSPDIF: {}\nAMP enabled: {}'.format(aux, rpi, spdif, amp_on))
            print(amp_rst)
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(PWR_EN_12V_PIN, 0)
GPIO.cleanup()
