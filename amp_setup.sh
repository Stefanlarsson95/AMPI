#!/bin/sh
echo "Amplifier IO setup"
sudo gpio -g mode 12 out
sudo gpio -g mode 13 out
#sudo gpio -g mode 23 out
#sudo gpio -g write 23 0
#sudo gpio -g pwm 12 450
sudo gpio -g write 12 1
sudo gpio -g write 13 1
#python /home/volumio/AMPI/hardware/pushconfig.py /home/volumio/AMPI/SigmaStudio/TxBuffer_IC_1.dat
#echo "Starting SigmaTCP server"
#/home/volumio/AMPI/sigma_tcp/sigma_tcp i2c /dev/i2c-1 0x34 &
sleep 1
#sudo gpio -g pwm 13 0 #600
#sudo gpio -g write 23 1
