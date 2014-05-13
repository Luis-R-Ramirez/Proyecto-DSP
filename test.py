__author__ = 'luis'


import numpy as np
import matplotlib.pyplot as plt


N = 1000.  # length
F = 1250.   # sample frequency
T = 1./F    # sample time
t = np.r_[0.:N]*T
F = np.zeros((N,20))
for K in range(0,20):
    F[:,K] = np.sin(2*np.pi*K*440*t)

plt.plot(t, F[:,2])
plt.show()

