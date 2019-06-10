The AMPI Project
=============

##### Base on:
https://github.com/usul27/hifiberry-dsp
https://github.com/diehardsk/Volumio-OledUI

## Instructions

#### Configure DPS
Run command:
````bash
python hardware/pushconfig.py SigmaStudio/TxBuffer_IC_1.dat
````

#### Check voltage
Power status. trottled: x50005 =  bad 0x50000 = good
````bash
vcgencmd get_throttled	
````


#### RPI Core temp

````bash
vcgencmd measure_temp
 ````

#### RPI AMP temp

````bash
cd /sys/bus/w1/devices
cd 28-02146367e1ff 
cat w1_slave
 ````


