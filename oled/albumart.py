#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Album art
"""

import time
import random
import os.path
from demo_opts import get_device
from luma.core.virtual import viewport
from PIL import Image


def main():
    images = [
        "pixelart1.png",
        "pixelart2.png",
        "pixelart3.jpg",
        "pixelart4.jpg",
        "pixelart5.jpg",
        "minutestomidnight2.jpg"

    ]

    while True:
        img_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
            'images', random.choice(images)))
        pixel_art = Image.open(img_path).convert(device.mode)
        w, h = pixel_art.size
        #w, h = 255, 63

        virtual = viewport(device, width=w, height=h)

        virtual.display(pixel_art)

        time.sleep(2)



if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
