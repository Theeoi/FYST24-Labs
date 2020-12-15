#!/usr/bin/python

import matplotlib.pyplot as plt

## Read in data from all three measurements

fileX523 = open("../Data/clean_SampleX532nmIntregared")
fileX523lines = fileX523.readlines()

energyX523 = []
countsX523 = []
for line in fileX523lines:
    energyX523.append(float(line.split(" ")[0]))
    countsX523.append(float(line.split(" ")[1]))

fileX523.close()

# ---

fileY523 = open("../Data/clean_SampleY532nmIntregared")
fileY523lines = fileY523.readlines()

energyY523 = []
countsY523 = []
for line in fileY523lines:
    energyY523.append(float(line.split(" ")[0]))
    countsY523.append(float(line.split(" ")[1]))

fileY523.close()

# ---

fileY720 = open("../Data/clean_SampleY720nm")
fileY720lines = fileY720.readlines()

energyY720 = []
countsY720 = []
for line in fileY720lines:
    energyY720.append(float(line.split(" ")[0]))
    countsY720.append(float(line.split(" ")[1]))

fileY720.close()

## Plot the data

plt.figure(figsize = (10,6))

plt.xlabel("Emission Energy [eV]", fontsize = "xx-large")
plt.ylabel("Counts [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(energyX523, countsX523)

plt.text(1.43, 10000, "3", fontsize = "x-large")
plt.text(1.50, 240000, "2", fontsize = "x-large")
plt.text(1.51, 100000, "1", fontsize = "x-large")
plt.text(1.73, 160000, "4", fontsize = "x-large")
plt.text(1.88, 30000, "5", fontsize = "x-large")

plt.savefig('../Fig/PLX523nm.png')
#plt.show()

# ---

plt.figure(figsize = (10,6))

plt.xlabel("Emission Energy [eV]", fontsize = "xx-large")
plt.ylabel("Counts [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(energyY523, countsY523)

plt.text(1.46, 20000, "Substrate", fontsize = "x-large", rotation = 45)
plt.text(1.56, 300000, "4", fontsize = "x-large")
plt.text(1.96, 30000, "5", fontsize = "x-large")

plt.savefig('../Fig/PLY523nm.png')
#plt.show()

# ---

plt.figure(figsize = (9,6))

plt.xlabel("Emission Energy [eV]", fontsize = "xx-large")
plt.ylabel("Counts [Arb. Unit]", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")

plt.plot(energyY720, countsY720)

plt.text(1.51, 2.0e6, "Substrate", fontsize = "x-large", rotation = 45)
plt.text(1.56, 1.5e6, "QW", fontsize = "x-large", rotation = 45)

plt.savefig('../Fig/PLY720nm.png')
#plt.show()




