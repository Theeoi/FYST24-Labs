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

plt.figure(figsize = (12,8))

plt.title("Coloumb Diamonds", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Source-Drain Voltage [mV]", fontsize = "x-large")

plt.pcolor(voltageG, voltageSD, current)
plt.show()
#plt.savefig('../Fig/ColoumbDiamonds.png')




