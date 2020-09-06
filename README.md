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
 
## ADAU1701 Installation
 Based on the guide and overlay from [digital-audio-labs.jimdofree.com](https://digital-audio-labs.jimdofree.com/english/raspberry-pi/adau1701-i2s-driver/)
 
 Big thanks to [MKSounds](https://github.com/MKSounds)!

Step1: Get overlay and copy to overlays folder
```bash
 git clone https://github.com/MKSounds/ADAU1701-I2S-Audio-Driver-for-Raspberry-Pi.git
```

Step2: Add overlay to overlay folder
```
sudo cp ADAU1701-I2S-Audio-Driver-for-Raspberry-Pi/adau1701-i2s.dtbo /boot/overlays
```
Step3: Add ADAU1701 to Volumio soundcards
Open soundcard JSON
```
sudo cp ADAU1701-I2S-Audio-Driver-for-Raspberry-Pi/adau1701-i2s.dtbo /boot/overlays
```
add ADAU1701 soundcard:
```
{"id":"adau1701-i2s","name":"ADAU1701 I2S Output","overlay":"adau1701-i2s","alsanum":"1","mixer":"Digital","modules":"","script":"","needsreboot":"yes"},
```
OBS: replace "Digital" with "" if Hardware volume is not used!

Step4: add dummy mixer to enable Hardware Volume

```shell script
state.Output {
	control.1 {
		iface MIXER
		name ADAU1701
		value.0 99
		value.1 99
		comment {
			access 'read write user'
			type INTEGER
			count 2
			range '0 - 99'
			tlv '00000001000000080000000000000032'
			dbmin 0
			dbmax 4950
			dbvalue.0 4950
			dbvalue.1 4950
		}
	}
}
```
 
 
 Finally reboot system
 
 ```bash
 reboot
 ```
