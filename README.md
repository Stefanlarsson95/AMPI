The AMPI Project
=============

##### Base on:
https://github.com/usul27/hifiberry-dsp

https://github.com/diehardsk/Volumio-OledUI

## Instructions

#### Configure DPS
Run command:
````bash
./AMPI/push_config.sh
````

#### Check voltage
Power status: 0x50005 =  bad, 0x50000 = good
````bash
sudo vcgencmd get_throttled	
````


#### RPI Core temp

````bash
sudo vcgencmd measure_temp
 ````

#### RPI AMP temp

````bash
cd /sys/bus/w1/devices
cd 28-02146367e1ff .
cat w1_slave
 ````

#### Instalation

### installation steps
```
sudo apt-get update
sudo apt-get install -y python-dev python-pip libfreetype6-dev libjpeg-dev build-essential python-rpi.gpio
sudo pip install --upgrade setuptools pip wheel
sudo pip install --upgrade socketIO-client-2 luma.oled
git clone https://github.com/Stefanlarsson95/AMPI
chmod +x ~/AMPI/ampi.py
sudo cp ~/AMPI/ampi.service /lib/systemd/system/
sudo cp ~/AMPI/dsp_config.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ampi.service
sudo systemctl enable dsp_config.service
reboot
```

 