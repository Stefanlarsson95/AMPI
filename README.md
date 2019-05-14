The AMPI Project
=============

Base on https://github.com/usul27/hifiberry-dsp


"HiFiBerry is a DSP board that has the same size at the Raspberry Pi. It can be plugged onto the Raspberry. 
It has a 2 channel analog input and 4 channel analog output. It can also be used as a sound card for the Raspberry Pi,
that means inputs and outputs from the DSP board can be routed to the I2S connector of the Raspberry Pi."

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

