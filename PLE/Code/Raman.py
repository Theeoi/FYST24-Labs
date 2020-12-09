#!/usr/bin/python

import matplotlib.pyplot as plt

## Read data

fileYRaman = open("../Data/clean_Raman")
fileYRamanlines = fileYRaman.readlines()

frequencyYRaman = []
countsYRaman = []
for line in fileYRamanlines:
    frequencyYRaman.append(float(line.split(" ")[0]))
    countsYRaman.append(float(line.split(" ")[1]))

fileYRaman.close()

## Plotting 

plt.figure(figsize = (9,6))

plt.xlabel("Frequency [Hz]", fontsize = "xx-large")
plt.ylabel("Counts [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(frequencyYRaman, countsYRaman)

plt.savefig('../Fig/Raman_Y.png')
#plt.show()
