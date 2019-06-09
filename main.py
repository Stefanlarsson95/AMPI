'''
    Main AMPI program

@author:     Stefan Larsson

@copyright:  2019 Stefan Larsson. All rights reserved.

@license:    license

@contact:    stefanlarsson95@gmail.com
@deffield    updated: 2019-02-03
'''
import sys
from hardware import adau1701 as DSP
from hardware import pushconfig, sigmaimporter





'''def print_header():
    header = CppHeaderParser.CppHeader('/home/pi/Documents/Python/AMPI/SigmaStudio/AMPI_1_IC_1_PARAM.h')
    #for defs in header.defines:
        #print " %s" % defs
    room = header.defines
    print room[5]'''


def main():
    print(DSP.read_back(0x00A6), DSP.read_back(0x0082), DSP.read_back(0x008E), DSP.read_back(0x009A))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
