import RPi.GPIO as GPIO
import modules.dsp_register as dsp_reg
import pathlib
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from modules.logger import *
from hardware import sigmaimporter
from threading import Lock, Event

# Setup
log = Log()
_path = str(pathlib.Path().absolute())
_root_path = _path.rsplit('/', 1)[0]
i2c_lock = Lock()
volume_event = Event()  # todo implement or remove
eq_event = Event()  # todo implement or remove

"""
General
"""
AMP_ALWAYS_OFF = True
emit_volume = False
emit_track = False
emit_shutdown = False
standby = False
mute = False
log.set_level(LOGLEVEL.INFO)

"""
Temp control
"""
AMP_TEMP_TARGET = 60
CPU_TEMP_TARGET = 60
CHASSIS_FAN_MAX_RPM = 5000
AMP_FAN_MAX_RPM = 4500

"""
Sources
"""
RPI_ENABLED = True
AUX_ENABLED = True
SPDIF_ENABLED = False
SOURCE_AUX = 0
SOURCE_RPI = 1
SOURCE_SPDIF = 2
SOURCE_AUTO = 3
INIT_SOURCE = None  # will read default from DSP
volumio_source = INIT_SOURCE

"""
GPIO config
"""
# Setup Mutual action pins
# pwr12v = POWER12V()

# Input
ACTIVITY_PIN = 0
ROT_ENTER_PIN = 5
ROT_A_PIN = 6
SPDIF_LOCK_PIN = 7
BTN_PREV = 17
BTN_NEXT = 9
AMPLIFIER_FAN_TACH_PIN = None
CHASSIS_FAN_TACH_PIN = 22
ROT_B_PIN = IR_PIN = 26
LRCLK_PIN = 19

# Output
SPDIF_ENABLE_PIN = 1
DSP_RST_PIN = 14
VOL_UP_PIN = 15
VOL_DN_PIN = 16
CHASSIS_FAN_PIN = 12
AMPLIFIER_FAN_PIN = 13
PWR_EN_12V_PIN = 23
AMP_EN_PIN = 27

"""
OlED/UI
"""
VOLUMIO_HOST = volumio_host = 'localhost'
VOLUMIO_PORT = volumio_port = 3000
VOLUME_DT = 5  # volume adjustment step

UPDATE_INTERVAL = 1 / 15  # 1/fps
STANDBY_UPDATE_INTERVAL = 1
PIXEL_SHIFT_TIME = 120  # time between picture position shifts in sec.

# todo merge to state class usage
STATE_NONE = -1
STATE_PLAYER = 0
STATE_PLAYLIST_MENU = 1
STATE_QUEUE_MENU = 2
STATE_VOLUME = 3
STATE_SHOW_INFO = 4
STATE_LIBRARY_MENU = 5
STATE_CLOCK = 6


class STATE:
    NONE = -1
    PLAYER = 0
    PLAYLIST_MENU = 1
    QUEUE = 2
    VOLUME = 3
    INFO_MENU = 4
    LIBRARY_MENU = 5
    CLOCK = 6
    EQ = 7
    EQ_MENU = 8
    SOURCE_MENU = 9


interface = spi(device=0, port=0)
oled = ssd1322(interface)

oled.WIDTH = 256
oled.HEIGHT = 64
oled.state = STATE_NONE
oled.state_default = STATE_CLOCK
oled.stateTimeout = 0
oled.update_interval = UPDATE_INTERVAL
oled.timeOutRunning = True
oled.activeSong = 'AMPI'
oled.activeArtist = 'VOLUMIO'
oled.playState = 'unknown'
oled.playPosition = 0
oled.ptime = 0
oled.pstart = 0
oled.duration = 0
oled.modal = None
oled.playlistoptions = []
oled.queue = []
oled.libraryFull = []
oled.libraryNames = []
oled.volume = 0
oled.volumeControlDisabled = False
oled.standby = False

"""
Sigma studio registers 
"""

_dsp_reg_adr = dsp_reg.get_reg(xml_path='/home/volumio/AMPI/SigmaStudio/AMPI_1.xml')

VOLUME_READ_REG = _dsp_reg_adr.get('master_volume.vol_redback')
AUX_DETECT_REG = _dsp_reg_adr.get('source_select.aux_signal_detect')
RPI_DETECT_REG = _dsp_reg_adr.get('source_select.rpi_signal_detect')
SPDIF_DETECT_REG = _dsp_reg_adr.get('source_select.spdif_signal_detect')
DSP_SOURCE_SELECT = _dsp_reg_adr.get('source_select.Input_selector')
CORE_REG = 0x081C
MUTE_BIT_MASK = 0b0010

"""
DSP conf
"""
DSP_DATA = sigmaimporter.read_txbuffer('/home/volumio/AMPI/SigmaStudio/TxBuffer_IC_1.dat')
DSP_SAMPLE_FREQ_LIM = 5

if __name__ == '__main__':
    print(_dsp_reg_adr)
