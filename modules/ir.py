#!/usr/bin/env python

import lirc
import time

sockid = lirc.init("ampi")
print 'ir test code'
while True:
    time.sleep(0.1)
    code = lirc.nextcode()
    for c in code:
        print c
lirc.deinit()