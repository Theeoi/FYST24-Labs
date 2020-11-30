#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Read Data for Blocked region
data1 = open("../Data/group4_log3.txt",'r')
data1Lines = data1.readlines()

voltage1 = []
current1 = []
for line in data1Lines[2:]:
    voltage1.append(float(line.split("\t")[1]))
    current1.append(float(line.split("\t")[2]))

data1.close()

# Read Data for non-Blocked region

data2 = open("../Data/group4_log4.txt",'r')
data2Lines = data2.readlines()

voltage2 = []
current2 = []
for line in data2Lines[2:]:
    voltage2.append(float(line.split("\t")[1]))
    current2.append(float(line.split("\t")[2]))

data2.close()

# Linear Fitting for Resistance

sIndex1 = np.argmin(np.abs(np.array(voltage1) - 0.0075))
Fit1Param = np.polyfit(voltage1[:sIndex1], current1[:sIndex1], 1)
Fit1 = np.poly1d(Fit1Param)
print("R1 = " + str(10**-6/Fit1Param[0]) + " MegaOhm")

xFit1 = np.linspace(voltage1[0], voltage1[-1], 50)
yFit1 = Fit1(xFit1)


Fit2Param = np.polyfit(voltage2, current2, 1)
Fit2 = np.poly1d(Fit2Param)
print("R2 = " + str(10**-6/Fit2Param[0]) + " MegaOhm")

xFit2 = np.linspace(voltage2[0], voltage2[-1], 50)
yFit2 = Fit2(xFit2)

#Plotting Blockade

plt.figure(figsize = (12,8))

plt.title("Coloumb Blockade", fontsize = "xx-large")
plt.xlabel("Source-Drain Voltage [mV]", fontsize = "x-large")
plt.ylabel("Tunneling Current [pA]", fontsize = "x-large")

plt.text(-5, 100, "$V_{G}$ = 3.08 V", fontsize = "x-large")

plt.xlim(voltage1[0] * 10**3, voltage1[-1] * 10**3)
plt.ylim(current1[-1] * 10**12, current1[0] * 10**12)

plt.plot([v * 10**3 for v in voltage1],[i * 10**12 for i in current1])
plt.plot([x * 10**3 for x in xFit1], [y * 10**12 for y in yFit1])
plt.gca().invert_xaxis()
#plt.show()
#plt.savefig('../Fig/ColoumbBlockade_Block.png')

#Plotting non-Blockade

plt.figure(figsize = (12,8))

plt.title("Coloumb non-Blockade", fontsize = "xx-large")
plt.xlabel("Source-Drain Voltage [mV]", fontsize = "x-large")
plt.ylabel("Tunneling Current [pA]", fontsize = "x-large")

plt.text(-5, 200, "$V_{G}$ = 3.16 V", fontsize = "x-large")

plt.xlim(voltage2[0] * 10**3, voltage2[-1] * 10**3)

plt.plot([v * 10**3 for v in voltage2],[i * 10**12 for i in current2])
plt.plot([x * 10**3 for x in xFit2], [y * 10**12 for y in yFit2])
plt.gca().invert_xaxis()
plt.show()
#plt.savefig('../Fig/ColoumbBlockade_nonBlock.png')



