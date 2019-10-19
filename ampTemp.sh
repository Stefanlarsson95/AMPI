#!/bin/sh
# if No W1 detected, add following to /boot/config.txt
# dtoverlay=w1–gpio
echo "Amplifier temp"
cat /sys/bus/w1/devices/28-02146367e1ff/w1_slave | tail -1 | cut -d'=' -f2