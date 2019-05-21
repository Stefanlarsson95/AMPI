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
from oled import scrolling_pixelart
import CppHeaderParser


# oled device config
device = ssd1322(spi(device=0, port=0))

# ADAU1701 configs


def print_header():
    header = CppHeaderParser.CppHeader('/home/pi/Documents/Python/AMPI/SigmaStudio/AMPI_1_IC_1_PARAM.h')
    #for defs in header.defines:
        #print " %s" % defs
    room = header.defines
    print room[5]
def main():
    print_header()
    #while True:
        #scrolling_pixelart.device = device
        #scrolling_pixelart.main()
        #albumart.device = device
        #albumart.main()
        #carousel.device=device
        #carousel.main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass