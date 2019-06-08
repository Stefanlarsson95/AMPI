#!/usr/bin/python -B
#
import eeprom
# import dsp_i2c
import adau1701
import sigmaimporter
import sys
import getopt
import time

sys.dont_write_bytecode = True

blocksize = 32
EEPROM = 1
DSP = 2


def write_device(data, destination=DSP, verbose=0):
    if destination == EEPROM:
        addr = 0

        code = sigmaimporter.txbuffer_data_to_eeprom(data);
        data.append(0)  # end code
        # split into 32 byte blocks
        while len(code) > 0:
            block = code[0:blocksize - 1]
            if (verbose):
                print block
            eeprom.eeprom_write_block(addr, block)
            code = code[blocksize:]
            addr += blocksize;
    elif destination == DSP:
        for block in data:
            addr = block["address"]
            data = block["data"]
            print "Writing {0} at {1:04X} ({1}), {2} byte".format(block["name"], addr, len(data))
            # dsp_i2c.dsp_write_block(addr,data,verbose)
            adau1701.dsp_write_block(addr, data, verbose)


def usage(myname):
    print "Usage: "
    print " {} [-e] [-v] [-t type]".format(myname)
    print "   -e: write to EEPROM instead of writing to the DSP itself"
    print "   -t: type: type of the DSP chip (only ADAU1701 supported today)"
    print "   -v: verbose"


def main(argv):
    myname = argv[0]
    destination = DSP
    verbose = 0

    try:
        opts, args = getopt.getopt(argv[1:], 'het:v')
    except getopt.GetoptError:
        usage(myname)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage(myname)
            sys.exit()
        elif opt in ("-e"):
            destination = EEPROM
        elif opt in ("-v"):
            verbose = 1
    try:
        file = args[0]
    except Exception:
        usage(myname)
        exit(2)

    data = sigmaimporter.read_txbuffer(file)
    if (len(data) == 0):
        print "Could not parse the {}".format(file)
        exit(1)

    write_device(data, destination, verbose)
    adau1701.close_i2c()


if __name__ == "__main__":
    main(sys.argv)

# mpv http://www.nasa.gov/mp3/590331main_ringtone_smallStep.mp3
# aplay -t raw -r 48000 -c 2 -f S16_LE /dev/zero
# vcgencmd get_throttled	// Power status. trottled=0x50005 =  bad 0x50000 = good
# sudo apt-get update
# sudo apt-get dist-upgrade

# // BanditRock
# vlc http://fm02-icecast.mtg-r.net/fm02_mp3

# // Core temp
# /opt/vc/bin/vcgencmd measure_temp
