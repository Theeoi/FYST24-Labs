#!/usr/bin/python

import matplotlib.pyplot as plt
import statistics

# Read the data into list.
data1 = open("../Data/group4_log1.txt",'r')
data1Lines = data1.readlines()

voltage1 = []
current1 = []
for line in data1Lines[2:]:
    voltage1.append(float(line.split("\t")[1]))
    current1.append(float(line.split("\t")[2]))

data1.close()

#ColoumbOscillation Zoomin

data2 = open("../Data/group4_log2.txt",'r')
data2Lines = data2.readlines()

voltage2 = []
current2_forward = []
current2_backward = []
for line in data2Lines[2:]:
    voltage2.append(float(line.split("\t")[1]))
    current2_forward.append(float(line.split("\t")[2]))
    current2_backward.append(float(line.split("\t")[3]))

data2.close()

#Plotting Full Oscillation scan

plt.figure(figsize = (12,8))

plt.title("Coloumb Oscillations", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Tunneling Current [pA]", fontsize = "x-large")

plt.text(2.3, 350, "$V_{SD}$ = 0.1 mV", fontsize = "x-large")

plt.xlim(2, voltage1[-1])

plt.plot(voltage1,[i * 10**12 for i in current1])
#plt.show()
plt.savefig('../Fig/ColoumbOscillations_Full.png')

#Plotting Oscillation Zoomin

plt.figure(figsize = (12,8))

plt.title("Coloumb Oscillations", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Tunneling Current [pA]", fontsize = "x-large")

plt.text(3.35, 30, "$V_{SD}$ = 0.05 mV", fontsize = "x-large")

plt.xlim(voltage2[0], voltage2[-1])

current2 = [statistics.mean(k) for k in zip(current2_forward, current2_backward)]
plt.plot(voltage2,[i * 10**12 for i in current2])
#plt.show()
plt.savefig('../Fig/ColoumbOscillations_Zoom.png')



