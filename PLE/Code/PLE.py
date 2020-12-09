#!/usr/bin/python

import matplotlib.pyplot as plt

## Read data

fileYPLE = open("../Data/clean_SampleYPLE799nm-709nm")
fileYPLElines = fileYPLE.readlines()

energyYPLE = []
countsYPLE = []
for line in fileYPLElines:
    energyYPLE.append(float(line.split(" ")[0]))
    countsYPLE.append(float(line.split(" ")[1]))

fileYPLE.close()

## Plotting 

plt.figure(figsize = (9,6))

plt.xlabel("Excitation Energy [eV]", fontsize = "xx-large")
plt.ylabel("Counts [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(energyYPLE, countsYPLE)

plt.savefig('../Fig/PLE_Y.png')
#plt.show()
