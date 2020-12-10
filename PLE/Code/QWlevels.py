#!/usr/bin/python

import matplotlib.pyplot as plt
import scipy
import scipy.constants as sp
import numpy as np

## Defining QW paramenter

me = 0.067 * sp.m_e
mlh = 0.082 * sp.m_e
mhh = 0.5 * sp.m_e

x_a = 2.5 * sp.nano
x_Vc = 0.219 * sp.e
x_Vv = 0.134 * sp.e

y_a = 10 * sp.nano
y_Vc = 0.271 * sp.e
y_Vv = 0.166 * sp.e

theta_tan1 = np.linspace(0, (1*sp.pi)/2, 100)
theta_cot1 = np.linspace((1*sp.pi)/2, (2*sp.pi)/2, 100)
theta_tan2 = np.linspace((2*sp.pi)/2, (3*sp.pi)/2, 100)
theta_cot2 = np.linspace((3*sp.pi)/2, (4*sp.pi)/2, 100)
theta_tan3 = np.linspace((4*sp.pi)/2, (5*sp.pi)/2, 100)
theta_cot3 = np.linspace((5*sp.pi)/2, (6*sp.pi)/2, 100)

theta = np.append(theta_tan1, theta_cot1, 0)
theta = np.append(theta, theta_tan2, 0)
theta = np.append(theta, theta_cot2, 0)
theta = np.append(theta, theta_tan3, 0)
theta = np.append(theta, theta_cot3, 0)

tan1 = np.tan(theta_tan1)
tan2 = np.tan(theta_tan2)
tan3 = np.tan(theta_tan3)
cot1 = - 1. / np.tan(theta_cot1)
cot2 = - 1. / np.tan(theta_cot2)
cot3 = - 1. / np.tan(theta_cot3)

## Calculating and plotting for Sample X

Xe_theta0 = (me * x_Vc * (x_a**2))/(2 * (sp.hbar**2))
Xlh_theta0 = (mlh * x_Vv * (x_a**2))/(2 * (sp.hbar**2))
Xhh_theta0 = (mhh * x_Vv * (x_a**2))/(2 * (sp.hbar**2))

Xe_sqrt = np.sqrt((Xe_theta0/(theta**2)) - 1)
Xlh_sqrt = np.sqrt((Xlh_theta0/(theta**2)) - 1)
Xhh_sqrt = np.sqrt((Xhh_theta0/(theta**2)) - 1)

plt.figure(figsize = (9,6))

plt.plot(theta_tan1, tan1, color = 'royalblue')
plt.plot(theta_cot1, cot1, color = 'royalblue')

plt.plot(theta, Xe_sqrt, color = 'limegreen', label = "Electron")
plt.plot(theta, Xlh_sqrt, color = 'forestgreen', label = "Light Hole")
plt.plot(theta, Xhh_sqrt, color = 'darkgreen', label = "Heavy Hole")

plt.ylim(0, 10)

plt.xlabel(r"$\theta = ka / 2$", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")
plt.legend(fontsize = "x-large")

plt.savefig("../Fig/X_QWlevels.png")
#plt.show()

## Calculating and plotting for Sample Y

Ye_theta0 = (me * y_Vc * (y_a**2))/(2 * (sp.hbar**2))
Ylh_theta0 = (mlh * y_Vv * (y_a**2))/(2 * (sp.hbar**2))
Yhh_theta0 = (mhh * y_Vv * (y_a**2))/(2 * (sp.hbar**2))

Ye_sqrt = np.sqrt((Ye_theta0/(theta**2)) - 1)
Ylh_sqrt = np.sqrt((Ylh_theta0/(theta**2)) - 1)
Yhh_sqrt = np.sqrt((Yhh_theta0/(theta**2)) - 1)

plt.figure(figsize = (9,6))

plt.plot(theta_tan1, tan1, color = 'royalblue')
plt.plot(theta_cot1, cot1, color = 'royalblue')
plt.plot(theta_tan2, tan2, color = 'royalblue')
plt.plot(theta_cot2, cot2, color = 'royalblue')
plt.plot(theta_tan3, tan3, color = 'royalblue')

plt.plot(theta, Ye_sqrt, color = 'limegreen', label = "Electron")
plt.plot(theta, Ylh_sqrt, color = 'forestgreen', label = "Light Hole")
plt.plot(theta, Yhh_sqrt, color = 'darkgreen', label = "Heavy Hole")

plt.ylim(0, 10)

plt.xlabel(r"$\theta = ka / 2$", fontsize = "xx-large")
plt.tick_params('both', labelsize="x-large")
plt.legend(fontsize = "x-large")

plt.savefig("../Fig/Y_QWlevels.png")
#plt.show()




