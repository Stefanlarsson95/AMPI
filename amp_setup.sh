#!/bin/sh
echo "Amplifier setup"
sudo gpio -g mode 12 pwm
sudo gpio -g mode 13 pwm
sudo gpio -g mode 23 out
sudo gpio -g mode 15 out
sudo gpio -g mode 16 out
#sudo gpio -g mode 27 out
sudo gpio -g write 23 0
#sudo gpio -g write 27 1
sudo gpio -g pwm 12 450
sudo gpio -g pwm 13 1000
python /home/volumio/AMPI/hardware/pushconfig.py /home/volumio/AMPI/SigmaStudio/TxBuffer_IC_1.dat
#echo "Starting SigmaTCP server"
#/home/volumio/AMPI/sigma_tcp/sigma_tcp i2c /dev/i2c-1 0x34 &
sleep 1
sudo gpio -g pwm 13 600
sudo gpio -g write 23 1
sleep 0.1
#sudo gpio -g write 27 0