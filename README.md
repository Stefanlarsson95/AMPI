The AMPI Project
=============

##### Base on:
https://github.com/usul27/hifiberry-dsp

https://github.com/diehardsk/Volumio-OledUI

## Scrips

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
The CPU core temp can be printed by the bash script:
````bash
~/AMPI/RpiTemp.sh
 ````

#### RPI AMP temp
The Amplifier heatsink temperature can med printed by the bash script:
````bash
~/AMPI/ampTemp.sh
 ````

## Instalation

#### installation steps
```bash
sudo apt update && sudo apt upgrade
sudo apt install -y python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential python3-rpi.gpio libatlas-base-dev
sudo pip3 install setuptools pip wheel
sudo pip3 install numpy
sudo pip3 install --upgrade socketIO-client3
sudo -H pip3 install --upgrade luma.oled
git clone https://github.com/Stefanlarsson95/AMPI
chmod +x ~/AMPI/AMPI.py ~/AMPI/push_config.sh ~/AMPI/RpiTemp.sh ~/AMPI/ampTemp.sh
sudo cp ~/AMPI/ampi.service /lib/systemd/system/
sudo cp ~/AMPI/dsp_config.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ampi.service
sudo systemctl enable dsp_config.service
```

 To enable the Oled display, SPI communication need to be enabled in the /boot/config.txt file.
 Add the following line.
 
 ```shell script
dtparam=spi=on
 ```
 
 Finally reboot system
 
 ```bash
 reboot
 ```