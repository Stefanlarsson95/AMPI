#!/usr/bin/python3

"""
Main AMPI code
"""

from __future__ import unicode_literals

import json
from cfg import *
import sys, atexit, signal
from socketIO_client import SocketIO
from time import time, sleep
from threading import Thread
from subprocess import run
from modules.rotaryencoder import RotaryEncoder
from modules.pushbutton import PushButton
from modules import volume
from modules.display import *
from modules.Input_selector import InputSelector
from modules.Shared import *
from hardware.pushconfig import write_device as Write_DSP

# atexit.register(defer) # fixme
# signal.signal(signal.SIGTERM, lambda n, f: sys.exit(0))

volumioIO = SocketIO(volumio_host, volumio_port)

# Todo create VolumioHandler and convert non screen variables to Volumio variable

image = Image.new('RGB', (oled.WIDTH + 4, oled.HEIGHT + 4))  # enlarged for pixelshift
oled.clear()

font = load_font('Roboto-Regular.ttf', 28)
font2 = load_font('PixelOperator.ttf', 15)
font3 = load_font('Roboto-Regular.ttf', 46)
font_stencil = load_font('stencil.ttf', 82)
hugefontaw = load_font('fa-solid-900.ttf', oled.HEIGHT - 18)


def display_update_service():
    pixshift = [2, 2]
    update_interval = UPDATE_INTERVAL
    lastshift = prevTime = time()
    while UPDATE_INTERVAL > 0:
        dt = time() - prevTime
        prevTime = time()
        if prevTime - lastshift > PIXEL_SHIFT_TIME:  # it's time for pixel shift
            lastshift = prevTime
            if pixshift[0] == 4 and pixshift[1] < 4:
                pixshift[1] += 1
            elif pixshift[1] == 0 and pixshift[0] < 4:
                pixshift[0] += 1
            elif pixshift[0] == 0 and pixshift[1] > 0:
                pixshift[1] -= 1
            else:
                pixshift[0] -= 1
        # auto return to home display screen (from volume display / queue list..)
        if oled.stateTimeout > 0:
            oled.timeOutRunning = True
            oled.stateTimeout -= dt
        elif oled.stateTimeout <= 0 and oled.timeOutRunning:
            oled.timeOutRunning = False
            oled.stateTimeout = 0
            SetState(STATE_PLAYER)

        elif not oled.standby and oled.playState == 'stop':  # Enter standby
            oled.standby = True
            SetState(STATE_CLOCK)
            update_interval = STANDBY_UPDATE_INTERVAL

        elif oled.standby and oled.playState != 'stop':  # Exit standby
            oled.standby = False
            SetState(STATE_PLAYER)
            update_interval = UPDATE_INTERVAL

        image.paste("black", [0, 0, image.size[0], image.size[1]])
        try:
            oled.modal.DrawOn(image)
        except AttributeError as e:
            log.err("render error", str(e))
        cimg = image.crop((pixshift[0], pixshift[1], pixshift[0] + oled.WIDTH, pixshift[1] + oled.HEIGHT))
        try:
            oled.display(cimg)
        except RuntimeError as e:
            log.err("RuntimeError: ", str(e))
        sleep(update_interval)


def SetState(state):
    oled.state = state
    if state == STATE_CLOCK:
        oled.contrast(100)
        sleep(0.1)
    else:
        oled.contrast(255)
        sleep(0.1)

    if oled.state == STATE_PLAYER:
        oled.modal = NowPlayingScreen(oled.HEIGHT, oled.WIDTH, oled.activeArtist, oled.activeSong, font, font2, font3,
                                      hugefontaw, oled.ptime, oled.duration)
        oled.modal.SetPlayingIcon(oled.playState, 10)
    elif oled.state == STATE_VOLUME:
        oled.modal = VolumeScreen(oled.HEIGHT, oled.WIDTH, oled.volume, font, font2)
    elif oled.state == STATE_PLAYLIST_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.playlistoptions, rows=3,
                                label='------ Select Playlist ------')
    elif oled.state == STATE_QUEUE_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.queue, rows=4, selected=oled.playPosition,
                                showIndex=True)
    elif oled.state == STATE_LIBRARY_MENU:
        oled.modal = MenuScreen(oled.HEIGHT, oled.WIDTH, font2, oled.libraryNames, rows=3,
                                label='------ Music Library ------')
    elif oled.state == STATE_CLOCK:
        oled.modal = ClockScreen(oled.HEIGHT, oled.WIDTH, font, font2, hugefontaw)
        oled.modal.SetPlayingIcon(oled.playState, 1)


def LoadPlaylist(playlistname):
    log.info("loading playlist: " + playlistname.encode('ascii', 'ignore'))
    oled.playPosition = 0
    volumioIO.emit('playPlaylist', {'name': playlistname})
    SetState(STATE_PLAYER)


def onPushState(data):
    global volumio_source
    newStatus = None
    if 'trackType' in data:
        s = data['trackType']
        if s != volumio_source:
            log.info("New source: " + str(s))
            volumio_source = s

    if 'title' in data:
        newSong = data['title']
    else:
        newSong = ''
    if newSong is None:
        newSong = ''

    if 'artist' in data:
        newArtist = data['artist']
    else:
        newArtist = ''
    if newArtist is None:  # volumio can push NoneType
        newArtist = ''

    if 'position' in data:  # current position in queue
        oled.playPosition = data['position']  # didn't work well with volumio ver. < 2.5

    if 'status' in data:
        newStatus = data['status']

    if 'seek' in data:
        oled.ptime = data['seek']
        oled.pstart = time() - oled.ptime / 1000

    if 'duration' in data:
        oled.duration = data['duration']

    if oled.state != STATE_VOLUME:  # get volume on startup and remote control
        try:  # it is either number or unicode text
            oled.volume = int(data['volume'])
        except (KeyError, ValueError):
            pass

    if 'disableVolumeControl' in data:
        oled.volumeControlDisabled = data['disableVolumeControl']

    if (newSong != oled.activeSong):  # new song
        # log.info("New Song: " + "\033[94m" + newSong.encode('ascii', 'ignore') + "\033[0m") todo fix error
        oled.activeSong = newSong
        oled.activeArtist = newArtist
        if hasattr(oled.modal, 'UpdatePlayingInfo') and newStatus != 'stop':
            oled.modal.UpdatePlayingInfo(newArtist, newSong)

    if newStatus != oled.playState:
        oled.playState = newStatus
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                iconTime = 25
            else:
                iconTime = 80
            try:
                oled.modal.SetPlayingIcon(oled.playState, iconTime)
            except:
                pass


def onPushQueue(data):
    oled.queue = [track['name'] if 'name' in track else 'no track' for track in data]
    log.info('Queue length is ' + str(len(oled.queue)))


def onPushBrowseSources(data):
    log.info('Browse sources:')
    for item in data:
        log.blue(item['uri'])


def onLibraryBrowse(data):
    oled.libraryFull = data
    itemList = oled.libraryFull['navigation']['lists'][0]['items']
    oled.libraryNames = [item['title'] if 'title' in item else 'empty' for item in itemList]
    SetState(STATE_LIBRARY_MENU)


def EnterLibraryItem(itemNo):
    selectedItem = oled.libraryFull['navigation']['lists'][0]['items'][itemNo]
    log.info("Entering library item: " + oled.libraryNames[itemNo].encode('ascii', 'ignore'))
    if selectedItem['type'][-8:] == 'category' or selectedItem['type'] == 'folder':
        volumioIO.emit('browseLibrary', {'uri': selectedItem['uri']})
    else:
        log.info("Sending new Queue")
        volumioIO.emit('clearQueue')  # clear queue and add whole list of items
        oled.queue = []
        volumioIO.emit('addToQueue', oled.libraryFull['navigation']['lists'][0]['items'])
        oled.stateTimeout = 5.0  # maximum time to load new queue
        while len(oled.queue) == 0 and oled.stateTimeout > 0.1:
            sleep(0.1)
        oled.stateTimeout = 0.2
        log.info("Play position = " + str(itemNo))
        volumioIO.emit('play', {'value': itemNo})


def LibraryReturn():  # go to parent category
    if not 'prev' in oled.libraryFull['navigation']:
        SetState(STATE_PLAYER)
    else:
        parentCategory = oled.libraryFull['navigation']['prev']['uri']
        log.info("Navigating to parent category in library: " + parentCategory.encode('ascii', 'ignore'))
        if parentCategory != '' and parentCategory != '/':
            volumioIO.emit('browseLibrary', {'uri': parentCategory})
        else:
            SetState(STATE_PLAYER)


def onPushListPlaylist(data):
    global oled
    if len(data) > 0:
        oled.playlistoptions = data


class TextScreen:
    def __init__(self, height, width, text, font):
        self.height = height
        self.width = width
        self.playingText = StaticText(self.height, self.width, text, font, center=True)
        self.textPos = (3, 6)

    def DrawOn(self, image):
        self.playingText.DrawOn(image, self.textPos)


class NowPlayingScreen:
    def __init__(self, height, width, row1, row2, font, font2, font3, fontaw, ptime, duration):
        self.height = height
        self.width = width
        self.font = font
        self.fontaw = fontaw
        self.playingText1 = StaticText(self.height, self.width, row1, font2, center=True)
        self.playingText2 = ScrollText(self.height, self.width, row2, font)
        self.icon = {'play': '\uf04b', 'pause': '\uf04c', 'stop': '\uf04d', 'mute': '\uf026', 'normalVol': '\uf027',
                     'highVol': '\uf028'}
        self.playingIcon = self.icon['play']
        self.volumeIcon = self.icon['mute']
        self.iconcountdown = 0
        self.text1Pos = (3, 6)
        self.text2Pos = (3, 21)  # 37
        self.barHeight = 4
        self.barWidth = width - 60  # 220
        self.seekBar = Bar(self.height, self.width, self.barHeight, self.barWidth)
        self.barPos = (30, 61)
        self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))
        self.duration = duration
        self.seekBar.SetFilledPercentage(50)
        self.ptime = 0
        self.played = 0

    def UpdatePlayingInfo(self, row1, row2):
        self.playingText1 = StaticText(self.height, self.width, row1, font2, center=True)
        self.playingText2 = ScrollText(self.height, self.width, row2, font)
        self.ptime = oled.ptime
        self.duration = oled.duration
        if self.ptime == 0:
            self.tStart = time()
        if oled.state != 'play':
            self.tStart = time() - float(self.ptime) / 1000

    def DrawOn(self, image):
        if oled.playState == 'play':
            t_now = float(time())
            self.ptime = (t_now - oled.pstart)
            if self.duration:  # Only Draw if duration data is received.
                self.played = float(self.ptime / self.duration) * 100
                self.seekBar.SetFilledPercentage(self.played)
                self.seekBar.DrawOn(image, self.barPos)

            self.playingText1.DrawOn(image, self.text1Pos)
            self.playingText2.DrawOn(image, self.text2Pos)

        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('RGBA'), self.alfaimage)
            image.paste(compositeimage.convert('RGB'), (0, 0))
            self.iconcountdown -= 1
        if oled.volume in range(1, 50):
            self.volumeIcon = ['normVol']
        elif oled.volume > 50:
            self.volumeIcon = ['highVol']
        else:
            self.volumeIcon = ['mute']

    def SetPlayingIcon(self, state, time=0):
        if state in self.icon:
            self.playingIcon = self.icon[state]
        self.alfaimage.paste((0, 0, 0, 0), [0, 0, image.size[0], image.size[1]])
        drawalfa = ImageDraw.Draw(self.alfaimage)
        iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=self.fontaw)
        left = (self.width - iconwidth) / 2
        drawalfa.text((left, 14), self.playingIcon, font=self.fontaw, fill=(255, 255, 255, 155))
        self.iconcountdown = time

    def NextOption(self):
        log.info("Play next")
        volumioIO.emit('next')

    def PrevOption(self):
        log.info("Play previous")
        volumioIO.emit('prev')


class ClockScreen:
    def __init__(self, height, width, font, font2, fontaw):
        self.height = height
        self.width = width
        self.font = font
        self.fontaw = fontaw
        self.playingText1 = StaticText(self.height, self.width, 'row1', font2, center=True)
        self.playingText2 = ScrollText(self.height, self.width, 'row2', font)
        self.icon = {'play': '\uf04b', 'pause': '\uf04c', 'stop': '\uf04d', 'mute': '\uf026', 'normalVol': '\uf027',
                     'highVol': '\uf028'}
        self.iconcountdown = 0
        self.text1Pos = (3, 6)
        self.text2Pos = (3, 21)  # 37

        self.alfaimage = Image.new('RGBA', image.size, (0, 0, 0, 0))

    def SetClock(self):
        # TODO remove date display and centering time.
        l_date = datetime.datetime.now().strftime("%D")
        l_time = datetime.datetime.now().strftime("%H:%M")
        self.playingText1 = StaticText(self.height + 5, self.width, l_date, font2, True)
        self.playingText2 = StaticText(self.height, self.width, l_time, font3, True)

    def DrawOn(self, image):

        self.SetClock()
        self.playingText1.DrawOn(image, self.text1Pos)
        self.playingText2.DrawOn(image, self.text2Pos)

        if self.iconcountdown > 0:
            compositeimage = Image.composite(self.alfaimage, image.convert('RGBA'), self.alfaimage)
            image.paste(compositeimage.convert('RGB'), (0, 0))
            self.iconcountdown -= 1

    def SetPlayingIcon(self, state, time=0):
        if state in self.icon:
            self.playingIcon = self.icon[state]
        self.alfaimage.paste((0, 0, 0, 0), [0, 0, image.size[0], image.size[1]])
        drawalfa = ImageDraw.Draw(self.alfaimage)
        iconwidth, iconheight = drawalfa.textsize(self.playingIcon, font=self.fontaw)
        left = (self.width - iconwidth) / 2
        drawalfa.text((left, 14), self.playingIcon, font=self.fontaw, fill=(255, 255, 255, 155))
        self.iconcountdown = time


class VolumeScreen:
    def __init__(self, height, width, volume, font, font2):
        self.height = height
        self.width = width
        self.font = font
        self.font2 = font2
        self.volumeLabel = None
        self.labelPos = (10, 3)
        self.volumeNumber = None
        self.numberPos = (225, 50)
        self.barHeight = 8
        self.barWidth = 195
        self.volumeBar = Bar(self.height, self.width, self.barHeight, self.barWidth)
        self.barPos = (30, 38)
        self.DisplayVolume(volume)
        self.volume = volume

    def DisplayVolume(self, vol):
        self.volume = vol
        self.volumeNumber = StaticText(self.height, self.width, str(vol) + '%', self.font2, True)
        self.volumeLabel = StaticText(self.height, self.width, 'Volume', self.font, True)
        self.volumeBar.SetFilledPercentage(vol)

    def DrawOn(self, img):
        self.volumeLabel.DrawOn(img, self.labelPos)
        self.volumeNumber.DrawOn(img, self.numberPos)
        self.volumeBar.DrawOn(img, self.barPos)


class MenuScreen:
    def __init__(self, height, width, font2, menuList, selected=0, rows=3, label='', showIndex=False):
        self.height = height
        self.width = width
        self.font2 = font2
        self.selectedOption = selected
        self.menuLabel = StaticText(self.height, self.width, label, self.font2, center=True)
        if label == '':
            self.hasLabel = 0
        else:
            self.hasLabel = 1
        self.labelPos = (1, 3)
        self.menuYPos = 3 + 16 * self.hasLabel
        self.menurows = rows
        self.menuText = [None for i in range(self.menurows)]
        self.menuList = menuList
        self.totaloptions = len(menuList)
        self.onscreenoptions = min(self.menurows, self.totaloptions)
        self.firstrowindex = 0
        self.showIndex = showIndex
        self.MenuUpdate()

    def MenuUpdate(self):
        self.firstrowindex = min(self.firstrowindex, self.selectedOption)
        self.firstrowindex = max(self.firstrowindex, self.selectedOption - (self.menurows - 1))
        for row in range(self.onscreenoptions):
            if (self.firstrowindex + row) == self.selectedOption:
                color = "black"
                bgcolor = "white"
            else:
                color = "white"
                bgcolor = "black"
            optionText = self.menuList[row + self.firstrowindex]
            if self.showIndex:
                width = 1 + len(str(self.totaloptions))  # more digits needs more space
                optionText = '{0:{width}d} {1}'.format(row + self.firstrowindex + 1, optionText, width=width)
            self.menuText[row] = StaticText(self.height, self.width, optionText, self.font2, fill=color,
                                            bgcolor=bgcolor)
        if self.totaloptions == 0:
            self.menuText[0] = StaticText(self.height, self.width, 'no items..', self.font2, fill="white",
                                          bgcolor="black")

    def NextOption(self):
        self.selectedOption = min(self.selectedOption + 1, self.totaloptions - 1)
        self.MenuUpdate()

    def PrevOption(self):
        self.selectedOption = max(self.selectedOption - 1, 0)
        self.MenuUpdate()

    def SelectedOption(self):
        return self.selectedOption

    def DrawOn(self, image):
        if self.hasLabel:
            self.menuLabel.DrawOn(image, self.labelPos)
        for row in range(self.onscreenoptions):
            self.menuText[row].DrawOn(image, (5, self.menuYPos + row * 16))
        if self.totaloptions == 0:
            self.menuText[0].DrawOn(image, (15, self.menuYPos))


def LeftKnob_RotaryEvent(dir):
    global emit_volume
    print(dir)

    if False and not oled.volumeControlDisabled and oled.state != STATE_PLAYLIST_MENU:
        if dir == RotaryEncoder.LEFT:
            oled.volume -= VOLUME_DT
            oled.volume = max(oled.volume, 0)
        elif dir == RotaryEncoder.RIGHT:
            oled.volume += VOLUME_DT
            oled.volume = min(oled.volume, 100)
        oled.stateTimeout = 2.0
        if oled.state != STATE_VOLUME:
            SetState(STATE_VOLUME)
        else:
            oled.modal.DisplayVolume(oled.volume)
        emit_volume = True


def LeftKnob_PushEvent(hold_time):
    global UPDATE_INTERVAL
    if hold_time < 3:
        log.blue('LeftKnob_PushEvent SHORT')
        if oled.state == STATE_PLAYER:
            if oled.playState == 'play':
                volumioIO.emit('stop')
            else:
                volumioIO.emit('play')
        if oled.state == STATE_PLAYLIST_MENU:
            SetState(STATE_PLAYER)
        if oled.state == STATE_LIBRARY_MENU:
            LibraryReturn()
    elif False:
        log.blue('LeftKnob_PushEvent LONG -> trying to shutdown')
        UPDATE_INTERVAL = 10  # stop updating screen
        sleep(0.1)
        show_logo("shutdown.ppm", oled)
        try:
            with open('oledconfig.json', 'w') as f:  # save current track number
                json.dump({"track": oled.playPosition}, f)
        except IOError as e:
            log.err('Cannot save config file to current working directory', str(e))
        sleep(1.5)
        # oled.cleanup()  # put display into low power mode
        # volumioIO.emit('shutdown')
        # sleep(60)


def RightKnob_RotaryEvent(dir):
    global emit_track
    if oled.state == STATE_PLAYLIST_MENU or oled.state == STATE_LIBRARY_MENU:
        oled.stateTimeout = 10.0
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()

    else:
        oled.stateTimeout = 3.0
        if oled.state != STATE_QUEUE_MENU:
            SetState(STATE_QUEUE_MENU)
        if dir == RotaryEncoder.LEFT:
            oled.modal.PrevOption()
        elif dir == RotaryEncoder.RIGHT:
            oled.modal.NextOption()
        oled.playPosition = oled.modal.SelectedOption()
        # emit_track = True


def RightKnob_PushEvent(hold_time):
    if hold_time < 1:
        log.blue('RightKnob_PushEvent SHORT')
        if oled.state == STATE_QUEUE_MENU:
            oled.stateTimeout = 0  # return to player mode
        elif oled.state != STATE_PLAYLIST_MENU and oled.state != STATE_LIBRARY_MENU:
            volumioIO.emit('listPlaylist')
            oled.stateTimeout = 20.0
            SetState(STATE_PLAYLIST_MENU)
            log.blue('Entering playlist menu')
        else:
            if oled.state == STATE_PLAYLIST_MENU:
                LoadPlaylist(oled.playlistoptions[oled.modal.SelectedOption()])
            if oled.state == STATE_LIBRARY_MENU:
                oled.stateTimeout = 20.0
                EnterLibraryItem(oled.modal.SelectedOption())
    else:
        log.blue('RightKnob_PushEvent LONG -> Music library browse')
        oled.stateTimeout = 20.0
        volumioIO.emit('browseLibrary', {'uri': 'music-library'})


"""
Startup initializer
"""
# LeftKnob_Push = PushButton(5, max_time=3)
# LeftKnob_Push.setCallback(LeftKnob_PushEvent)
# LeftKnob_Rotation = RotaryEncoder(6, 26, pulses_per_cycle=4)
# LeftKnob_Rotation.setCallback(LeftKnob_RotaryEvent)

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


def _receive_thread():
    volumioIO.wait()


receive_thread = Thread(target=_receive_thread, name="Receiver")
receive_thread.daemon = True

volumioIO.on('pushState', onPushState)
volumioIO.on('pushListPlaylist', onPushListPlaylist)
volumioIO.on('pushQueue', onPushQueue)
volumioIO.on('pushBrowseSources', onPushBrowseSources)
# Todo test below
# volumioIO.on('pushBrowseLibrary', onLibraryBrowse)

# get list of Playlists and initial state
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
    global emit_volume, emit_track
    while True:
        if oled.standby:
            sleep(0.5)
        else:
            if emit_volume:
                emit_volume = False
                volume.sw_volume = oled.volume
                log.info("SW volume: " + str(oled.volume))
                volumioIO.emit('volume', oled.volume)
                SetState(STATE_VOLUME)
                oled.stateTimeout = 0.01
            elif oled.state == STATE_PLAYER and volume.update_volume():
                volume.emit_volume = False
                oled.volume = volume.hw_volume
                volumioIO.emit('volume', oled.volume)
                SetState(STATE_VOLUME)  # Todo Fix hw hysteres
                oled.stateTimeout = 1

            if emit_track and oled.stateTimeout < 4.5:
                emit_track = False
                try:
                    log.info(
                        'Track selected: ' + str(oled.playPosition + 1) + '/' + str(len(oled.queue)) + ' ' + oled.queue[
                            oled.playPosition].encode('ascii', 'ignore'))
                except IndexError:
                    pass
                volumioIO.emit('play', {'value': oled.playPosition})

            sleep(UPDATE_INTERVAL)


def defer():
    global UPDATE_INTERVAL
    try:
        show_logo("shutdown.ppm", oled)
        UPDATE_INTERVAL = 10
        sleep(2)
        oled.cleanup()
        input_selector.stop()
        print('\n')
        log.info("System exit ok")

    except Exception as err:
        log.err("Defer Error: " + str(err))


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        defer()

# Todo
#  Fix auto pushconfig() if no code is on DPS
#  Logging to file
#  test:
#       import sys
#       signal.signal(signal.SIGTERM, lambda num, frame: sys.exit(0))
