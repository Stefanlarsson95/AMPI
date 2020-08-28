import RPi.GPIO as GPIO
import modules.dsp_register as dsp_reg
import pathlib
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322

"""
General
"""
_path = str(pathlib.Path().absolute())
_root_path = _path.rsplit('/', 1)[0]

"""
GPIO setup
"""
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Input
ACTIVITY_PIN = 0
SPDIF_LOCK_PIN = 7

# Output conf
DPS_WP_PIN = 14
VOL_DN_PIN = 15
VOL_UP_PIN = 16
CHASSIS_FAN_PIN = 12
AMPLIFIER_FAN_PIN = 13
AMPLIFIER_FAN_TAC_PIN = 25
AMPLIFIER_ENABLE_PIN = 27
PWR_EN_12V_PIN = 23

# Setup GPIO
GPIO .setwarnings(False)
GPIO.setup([PWR_EN_12V_PIN,
            VOL_DN_PIN,
            VOL_UP_PIN,
            CHASSIS_FAN_PIN,
            AMPLIFIER_FAN_PIN,
            AMPLIFIER_ENABLE_PIN], GPIO.OUT)  # Setup outputs
GPIO.setwarnings(True)
GPIO.setup([SPDIF_LOCK_PIN,
            ACTIVITY_PIN], GPIO.IN)                    # Setup inputs
GPIO.output([VOL_UP_PIN,
             VOL_DN_PIN,
             PWR_EN_12V_PIN], 0)                    # Ensure volume pot is not moved

"""
OlED/UI
"""
volumio_host = 'localhost'
volumio_port = 3000
VOLUME_DT = 5  # volume adjustment step

UPDATE_INTERVAL = 0.034
STANDBY_UPDATE_INTERVAL = 1
PIXEL_SHIFT_TIME = 120  # time between picture position shifts in sec.

STATE_NONE = -1
STATE_PLAYER = 0
STATE_PLAYLIST_MENU = 1
STATE_QUEUE_MENU = 2
STATE_VOLUME = 3
STATE_SHOW_INFO = 4
STATE_LIBRARY_MENU = 5
STATE_CLOCK = 6

interface = spi(device=0, port=0)
oled = ssd1322(interface)

oled.WIDTH = 256
oled.HEIGHT = 64
oled.state = STATE_NONE
oled.stateTimeout = 0
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
Sigma studio register config
"""

#_dsp_reg_adr = dsp_reg.get_reg(xml_path=str(_root_path + '/SigmaStudio/AMPI_1.xml'))
_dsp_reg_adr = dsp_reg.get_reg(xml_path='/home/volumio/AMPI/SigmaStudio/AMPI_1.xml')

VOLUME_READ_REG = _dsp_reg_adr.get('master_volume.vol_redback')
AUX_DETECT_REG = _dsp_reg_adr.get('source_select.aux_signal_detect')
RPI_DETECT_REG = _dsp_reg_adr.get('source_select.rpi_signal_detect')
SPDIF_DETECT_REG = _dsp_reg_adr.get('source_select.spdif_signal_detect')


if __name__ == '__main__':
    print(_dsp_reg_adr)
