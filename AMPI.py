#!/usr/bin/python3

"""
Main AMPI code
"""

from __future__ import unicode_literals
from cfg import *
import json
import sys, atexit, signal
from socketIO_client import SocketIO
from modules.ampi_backend import *
from time import time, sleep
from threading import Thread
from subprocess import run
from modules.rotaryencoder import RotaryEncoder
from modules.pushbutton import PushButton
# from modules.volumecontroller import *
from modules.display import *
from modules.Input_selector import InputSelector
from modules import temp_controller as temp_ctrl
from modules.shared import *
from modules import runtime_cli as rtcli

# from hardware.pushconfig import write_device as Write_DSP
GPIO.setmode(GPIO.BCM)

"""
Startup initializer
"""

oled.clear()

show_logo("volumio_logo.ppm", oled)

# Push configfile to DSP
# Write_DSP(DSP_DATA, 2, verbose=False)
# oled.modal = TextScreen(oled.HEIGHT - 10, oled.WIDTH, 'AMPI', font_stencil)
oled.modal = ampi_logo()
oled.stateTimeout = 2

# Start threads
receive_thread.start()
screen_update_thread.start()

# Start Controllers
input_selector = InputSelector().start()
volume_controller.start()
temp_ctrl.start()

rtcli.init([temp_ctrl.read_cpu_temp,
            temp_ctrl.read_amp_temp,
            temp_ctrl.disp_temp,
            input_selector.get_dsp_source,
            volume_controller.get_volume,
            volume_controller.set_volume,
            volume_controller.get_volume_source])

# startup sound fixme source select not working!
# input_selector.set_dsp_source(SOURCE_RPI)
# amp.set()
sleep(0.5)
# run(["aplay --device plughw:CARD=1 ./startup.wav"], shell=True)
sleep(1.5)
# amp.release()
# input_selector.set_dsp_source(SOURCE_AUTO)

# Request Volumio Data
volumioIO.emit('listPlaylist')
volumioIO.emit('getState')
volumioIO.emit('getQueue')
# volumioIO.emit('getBrowseSources')
sleep(0.1)

try:
    with open('oledconfig.json', 'r') as f:  # load last playing track number
        config = json.load(f)
except IOError:
    pass
else:
    oled.playPosition = config['track']


# todo redo runtime event handling using threading.Even()
def main():
    global emit_track, state_default
    _playState = None
    while True:
        # if inactive, set in standby
        # todo impl function changing pause -> stop if timeout passed ?
        if not oled.standby and oled.playState in ['stop', 'pause']:
            oled.standby = True
            oled.state_default = STATE.CLOCK
            oled.stateTimeout = 0.1

        # standby state
        if oled.standby \
                and not emit_volume \
                and not volume_controller.emit_volume \
                and not GPIO.input(ACTIVITY_PIN) \
                and oled.playState in ['stop', 'pause']:
            oled.update_interval = STANDBY_UPDATE_INTERVAL
            sleep(1)
        else:
            oled.update_interval = UPDATE_INTERVAL
            oled.standby = False
            # Handle playing state change
            if _playState != oled.playState:
                _playState = oled.playState
                if _playState == 'play':
                    oled.state_default = STATE_PLAYER
                    oled.stateTimeout = 0.1

            # Handle Volume event
            if volume_controller.emit_volume:
                vol = volume_controller.get_volume()
                log.info("Volume: " + str(vol))
                volumioIO.emit('volume', vol)
                oled.volume = vol
                if oled.state != STATE_VOLUME:
                    SetState(STATE_VOLUME)
                else:
                    oled.modal.DisplayVolume(oled.volume)
                volume_controller.emit_volume = False

            # Handle track change event
            if emit_track and oled.stateTimeout < 4.5:  # todo change to standby check?
                emit_track = False
                try:
                    log.info(
                        'Track selected: ' + str(oled.playPosition + 1) + '/' + str(len(oled.queue)) + ' ' + oled.queue[
                            oled.playPosition].encode('ascii', 'ignore'))
                except IndexError:
                    pass
                volumioIO.emit('play', {'value': oled.playPosition})

            sleep(0.025)


def shutdown():
    global emit_shutdown
    emit_shutdown = True
    GPIO.setwarnings(False)
    oled.update_interval = -1  # Stop updating screen
    oled.stateTimeout = 10
    show_logo("shutdown.ppm", oled)
    input_selector.stop()
    amp.release(enforce=True)
    # GPIO.setup(AMP_EN_PIN, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(PWR_EN_12V_PIN, GPIO.OUT, initial=GPIO.LOW)
    sleep(2)
    oled.cleanup()
    log.info("System exit ok")


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        shutdown()

# todo necessary?
# atexit.register(shutdown)
# signal.signal(signal.SIGTERM, lambda n, f: sys.exit(0))
