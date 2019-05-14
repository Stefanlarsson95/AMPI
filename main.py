'''
    Main AMPI program

@author:     Stefan Larsson

@copyright:  2019 Stefan Larsson. All rights reserved.

@license:    license

@contact:    stefanlarsson95@gmail.com
@deffield    updated: 2019-02-03
'''


from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from oled import animated_gif, clock, font_awesome, sprite_animation, perfloop, greyscale, scrolling_pixelart, welcome, albumart, carousel
import time
import subprocess


# oled device config
device = ssd1322(spi(device=0, port=0))


def main():

    while True:
        #scrolling_pixelart.device = device
        #scrolling_pixelart.main()
        #albumart.device = device
        #albumart.main()
        carousel.device=device
        carousel.main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass