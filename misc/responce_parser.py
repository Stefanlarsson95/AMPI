import numpy as np
from os import getcwd

fileName = 'TEST_RESPONSE'
filePath = getcwd() + '\\' + fileName + '.txt'

fout = open(getcwd() + '\\' + fileName + '_MLSSA.txt', 'w')

# Sigma Studio Required Spacing Placement
fout.write('Example Header Line; this can be anything you want...\n')
fout.write('      "Hz"  "Mag (dB)"       "deg"\n')

# Load in data, skip the header.
# REW has 14 lines of header info
data = np.genfromtxt(filePath, skip_header=14, delimiter=' ')

for i in range(0, len(data)):
    fout.write('{0:10}, {1:11}, {2:11}\n'.format(data[i, 0], data[i, 1], data[i, 2]))

fout.close()
print('Conversion Complete!')