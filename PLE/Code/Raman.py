#!/usr/bin/python

import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def GaAs(x):
    return 291.50 - 42.10*x + 4.47*x**2 - 296

def AlAs(x):
    return 360.52 + 58.15*x - 15.87*x**2 - 386

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

plt.xlabel("Frequency [$cm^{-1}$]", fontsize = "xx-large")
plt.ylabel("Intensity [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(frequencyYRaman, countsYRaman)

plt.text(300, 0.6, "GaAs", fontsize = "x-large")
plt.text(390, 0.7, "AlAs", fontsize = "x-large")

plt.savefig('../Fig/Raman_Y.png')
#plt.show()

print(fsolve(GaAs, 0.35))
print(fsolve(AlAs, 0.35))
