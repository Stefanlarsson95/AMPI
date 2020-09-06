#!/usr/bin/env python3

import lirc
import time

sockid = lirc.init("ampi")
print('ir test code')
try:
    while True:
        time.sleep(0.1)
        code = lirc.nextcode()
        for c in code:
            print(c)
except:
    pass
lirc.deinit()
