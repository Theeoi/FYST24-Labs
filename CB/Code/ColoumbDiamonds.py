#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

# Read Data
data1 = open("../Data/group4_log5.txt",'r')
data1Lines = data1.readlines()

voltageSD = []
current1 = []
for line in data1Lines[2:]:
    voltageSweep.append(float(line.split("\t")[1]))
    current1.append(float(line.split("\t")[2]))

data1.close()

#Plotting

plt.figure(figsize = (12,8))

plt.title("Coloumb Diamonds", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Source-Drain Voltage [mV]", fontsize = "x-large")

plt.pcolor(voltageG, voltageSD, current)
plt.show()
#plt.savefig('../Fig/ColoumbDiamonds.png')




