#!/bin/sh
echo "Amplifier setup"
sudo gpio -g mode 12 pwm
sudo gpio -g mode 13 pwm
sudo gpio -g mode 23 out
sudo gpio -g mode 27 out
sudo gpio -g write 23 1
sudo gpio -g write 27 0
sudo gpio -g pwm 12 450
sudo gpio -g pwm 13 1000
sleep 1
sudo gpio -g pwm 13 600
