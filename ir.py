#!/usr/bin/env python

import lirc
import time

sockid = lirc.init("ampi")

while True:
    #print "waitning for keypress"
    time.sleep(0.1)
    code = lirc.nextcode()
    if code != []:
        print code[0]
lirc.deinit()