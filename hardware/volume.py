import adau1701 as DSP

VOL_READBACK_HIGH = 0x00
VOL_READBACK_LOW = 0xA6

class Volume:
    def __init__(self, volume, hw_volume=0, sw_volume=0, balance=0):
        if hw_volume == 0:
            self.hw_volume = self.read_hw_vol()
        else:
            self.hw_volume = hw_volume
        self.volume = hw_volume
        self.hw_volume = hw_volume
        self.sw_volume = sw_volume
        self.balance = balance

    def read_hw_vol(self):
        return DSP.read_back(VOL_READBACK_HIGH, VOL_READBACK_LOW)


