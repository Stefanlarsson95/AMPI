import RPi.GPIO as GPIO
import modules.dsp_register as dsp_reg
import pathlib

"""
General
"""

_root_path = str(pathlib.Path().absolute())

"""
GPIO setup
"""

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

# Input conf
SPDIF_LOCK_PIN = 7

# Output conf
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
GPIO.setup([SPDIF_LOCK_PIN], GPIO.IN)                    # Setup inputs
GPIO.output([VOL_UP_PIN,
             VOL_DN_PIN,
             PWR_EN_12V_PIN], 0)                    # Ensure volume pot is not moved

"""
Sigma studio register config
"""

_dsp_reg_adr = dsp_reg.get_reg(xml_path=(_root_path + '/SigmaStudio/AMPI_1.xml'))

VOLUME_READ_REG = _dsp_reg_adr.get('master_volume.vol_redback')
AUX_DETECT_REG = _dsp_reg_adr.get('source_select.aux_detect')
RPI_DETECT_REG = _dsp_reg_adr.get('source_select.rpi_detect')
SPDIF_DETECT_REG = _dsp_reg_adr.get('source_select.spdif_detect')

print(_dsp_reg_adr)