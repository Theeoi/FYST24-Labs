#!/usr/bin/python

import matplotlib.pyplot as plt

# Read the data into list.
data = open("../Data/group4_log1.txt",'r')
dataLines = data.readlines()

voltage = []
current = []
for line in dataLines[2:]:
    voltage.append(float(line.split("\t")[1]))
    current.append(float(line.split("\t")[2]))

data.close()
newCurrent = [i * 10**12 for i in current] #Multiplying current to read pA instead of A.

plt.figure(figsize = (12,8))

plt.title("Coloumb Oscillations", fontsize = "xx-large")
plt.xlabel("Gate Voltage [V]", fontsize = "x-large")
plt.ylabel("Tunneling Current [pA]", fontsize = "x-large")

plt.text(2.3, 350, "$V_{SD}$ = 0.1 mV", fontsize = "x-large")

plt.xlim(2, voltage[-1])

plt.plot(voltage,newCurrent)
plt.show()

