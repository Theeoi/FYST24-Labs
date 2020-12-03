#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Read Data
data1 = open("../Data/group4_log5.txt",'r')
data1Lines = data1.readlines()

voltageG = np.array(data1Lines[0].split("\t")[2:], float)

A = np.zeros((101, len(voltageG)+2))

k = 0
for line in data1Lines[2:]:
    A[k] = np.array(line.split("\t"), float)
    k += 1

data1.close()

voltageSD = A[:,1]
current = A[:,2:]

#Plotting

plt.figure(figsize = (9,6))

#plt.title("Coloumb Diamonds", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Source-Drain Voltage [mV]", fontsize = "x-large")
plt.tick_params('both', labelsize="large")

plt.pcolor(voltageG, [v * 10**3 for v in voltageSD], [i * 10**12 for i in current], cmap='RdBu', shading='auto')
cb = plt.colorbar()
cb.set_label("Current [pA]", fontsize = "x-large")
cb.ax.tick_params('both', labelsize="large")
#plt.show()
plt.savefig('../Fig/ColoumbDiamonds.png')




