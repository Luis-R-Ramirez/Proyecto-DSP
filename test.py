__author__ = 'luis'


import numpy as np
import matplotlib.pyplot as plt


N = 1000.
t = np.r_[0.:N]/1250
F = np.zeros((N,20))
for K in range(0,20):
    F[:,K] = np.sin(2*np.pi*t*K*440)

plt.plot(t, F[:,6])
plt.show()

