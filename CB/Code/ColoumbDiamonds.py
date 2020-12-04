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

plt.figure(figsize = (7,9))

plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Source-Drain Voltage [mV]", fontsize = "x-large")
plt.tick_params('both', labelsize="large")

plt.xlim(3.55, 3.69)

plt.plot([3.56, 3.68],[0,0], marker='o')
plt.text(3.60, 0.25, "$\Delta V_g$ = 0.12 V", fontsize = "x-large")

plt.plot([3.615, 3.615],[0, -6.5], marker='o')
plt.text(3.618, -5, "$\Delta V_{sd}$ = 6.5 mV", fontsize = "x-large", rotation=90)

plt.pcolor(voltageG, [v * 10**3 for v in voltageSD], [i * 10**12 for i in current], cmap='RdBu', shading='auto')
cb = plt.colorbar()
cb.set_label("Current [pA]", fontsize = "x-large")
cb.ax.tick_params('both', labelsize="large")

#plt.show()
plt.savefig('../Fig/ColoumbDiamond_Zoom.png')




