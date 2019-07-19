import lirc, time
import multiprocessing  #import Process,Value,Array ,Manager,Lock;
from modules import OLED
from modules import logger, volume as Vol
import math
log = logger.Log(logger.LOGLEVEL.INFO)
vol = Vol.VOLUME()
oled = OLED.oled
_Oled_Process = multiprocessing.Process(name='OLED', target=OLED.main_process, args=())
_Volume_Process = multiprocessing.Process(name='VOLUME', target=vol.run, args=())
tInit = time.time()

sockid = lirc.init("ampi", blocking=False)


def init():
    _Oled_Process.start()
    _Volume_Process.start()

def main():
    init()
    while True:
        t = time.time()
        log.info("Ampi Time: " + str(t))
        time.sleep(0.1)


if __name__ == '__main__':
    main()












'''
def check_volume():
    global emit_volume
    if vol._t_scan + vol.update_hw_interval < time.time() and abs(
            oled.volume - vol.get_hw_vol()) > vol._VOL_ERR_HYSTERES:  # New hardware volume -> set remote volume
        vol.update_hw_interval = 0.1
        vol.volume = vol._hw_volume
        emit_volume = True
    elif not oled.volume == vol.volume:  # New remote volume -> set hardware volume
        vol.set_hw_vol(oled.volume)
        vol.volume = oled.volume
    else:  # same volume
        if oled.state != STATE_VOLUME:
            vol.update_hw_interval = 1
        return False

    if oled.state != STATE_PLAYLIST_MENU:
        oled.stateTimeout = 2.0
        if oled.state != STATE_VOLUME:
            SetState(STATE_VOLUME)
        else:
            try:
                oled.modal.DisplayVolume(oled.volume)
            except AttributeError as msg:
                print("Error Displaying volume! ", msg)
    return True  # new volume event
'''