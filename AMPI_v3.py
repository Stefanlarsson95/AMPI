#!/usr/bin/python3

"""
Main AMPI code
"""

from __future__ import unicode_literals

import json
from cfg import *
import sys, atexit, signal
from socketIO_client import SocketIO
from modules.ampi_backend import *
from time import time, sleep
from threading import Thread
from subprocess import run
from modules.rotaryencoder import RotaryEncoder
from modules.pushbutton import PushButton
from modules import volume
from modules.display import *
from modules.Input_selector import InputSelector
from modules.shared import *
from hardware.pushconfig import write_device as Write_DSP

"""
Startup initializer
"""
# LeftKnob_Push = PushButton(5, max_time=3)
# LeftKnob_Push.setCallback(LeftKnob_PushEvent)
# LeftKnob_Rotation = RotaryEncoder(6, 26, pulses_per_cycle=4)
# LeftKnob_Rotation.setCallback(LeftKnob_RotaryEvent)
oled.clear()

if not GPIO.input(SPDIF_LOCK_PIN):
    GPIO.output(PWR_EN_12V_PIN, 1)
    sleep(0.1)
else:
    GPIO.output(PWR_EN_12V_PIN, 0)
GPIO.output(AMPLIFIER_ENABLE_PIN, 1)  # enable amplifier for startup melody

RightKnob_Push = PushButton(ROT_ENTER_PIN, max_time=1)
RightKnob_Push.setCallback(RightKnob_PushEvent)
RightKnob_Rotation = RotaryEncoder(ROT_A_PIN, ROT_B_PIN, pulses_per_cycle=4)
RightKnob_Rotation.setCallback(RightKnob_RotaryEvent)
show_logo("volumio_logo.ppm", oled)

# Push configfile to DSP
# Write_DSP(DSP_DATA, 2, verbose=False)

sleep(0.5)
# run(["aplay --device plughw:CARD=1 ./startup.wav"], shell=True)
sleep(1.5)

oled.modal = TextScreen(oled.HEIGHT - 10, oled.WIDTH, 'AMPI', font_stencil)
oled.stateTimeout = 2

screen_update_thread = Thread(target=display_update_service, name="Screen updater")
screen_update_thread.daemon = True

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

# Start threads
receive_thread.start()
screen_update_thread.start()
input_selector = InputSelector().start()


def main():
    global emit_volume, emit_track, state_default
    _playState = None
    while True:

        # if inactive, set in standby
        if not oled.standby and oled.playState in ['stop', 'pause']:
            oled.state_default = STATE_CLOCK
            oled.stateTimeout = 0.1
            oled.standby = True

        if oled.standby \
                and not emit_volume \
                and not emit_track \
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
            if emit_volume:  # HW volume change
                volume.sw_volume = oled.volume
                log.info("SW volume: " + str(oled.volume))
                volumioIO.emit('volume', oled.volume)
                if oled.state != STATE_VOLUME:
                    SetState(STATE_VOLUME)
                else:
                    oled.modal.DisplayVolume(oled.volume)
                oled.stateTimeout = 0.5
            elif oled.volume != volume.sw_volume:  # SW volume change
                pass

            # Handle track change event
            if emit_track and oled.stateTimeout < 4.5:
                emit_track = False
                try:
                    log.info(
                        'Track selected: ' + str(oled.playPosition + 1) + '/' + str(len(oled.queue)) + ' ' + oled.queue[
                            oled.playPosition].encode('ascii', 'ignore'))
                except IndexError:
                    pass
                volumioIO.emit('play', {'value': oled.playPosition})

            sleep(0.025)


def shutdown(emit_shutdown=False):
    try:
        oled.update_interval = 0.01
        show_logo("shutdown.ppm", oled)
        oled.stateTimeout = 10
        sleep(2)
        input_selector.stop()
        oled.cleanup()
        oled.update_interval = 0
        print('\n')
        log.info("System exit ok")
    except Exception as err:
        log.err("Shutdown Error: " + str(err))

    if emit_shutdown:
        pass
        # volumioIO.emit('shutdown')
        # sleep(60)


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        shutdown()

atexit.register(shutdown)
signal.signal(signal.SIGTERM, lambda n, f: sys.exit(0))
