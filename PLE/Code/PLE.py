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

plt.plot(energyYPLE, countsYPLE, label = "PLE Spectrum")

plt.vlines(1.559, 1120, 1200, colors = 'm', label = "n = 1") # n1 hh
plt.vlines(1.578, 1120, 1200, colors = 'm') # n1 lh
plt.vlines(1.672, 1120, 1200, colors = 'y', label = "n = 2") # n2 hh
plt.vlines(1.746, 1120, 1200, colors = 'y') # n2 lh

#plt.vlines(1.604, 1120, 1200, colors = 'teal') # n13 hh
#plt.vlines(1.740, 1120, 1200, colors = 'teal') # n24 3h

plt.legend(fontsize = 'x-large', loc = 4)

plt.savefig('../Fig/PLE_Y.png')
#plt.show()
