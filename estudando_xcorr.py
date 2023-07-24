# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:02:43 2023

@author: LOFEC-AIRMOD

Link: https://acervolima.com/matplotlib-pyplot-xcorr-em-python/
"""


import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
# import statsmodels.api as sm

# First signal 
sig1 = np.sin(np.r_[-10:0:0.1])

# Seconds signal with pi/4 phase shift. Half the size of sig1
sig2 = np.sin(np.r_[-10:0:0.1] + np.pi/4)

fig, ax = plt.subplots(2, 1)


ax[0].plot(np.arange(-10.0, 0.0, 0.1), sig1)

ax[0].plot(np.arange(-10.0, 0.0, 0.1), sig2)

ax[0].set_xlim(-12, 12)

# Pre-allocate correlation array
# corr = (len(sig1) - len(sig2) + 1) * [0]

# Go through lag components one-by-one
# for l in range(len(corr)):
#    corr[l] = sum([sig1[i+l] * sig2[i] for i in range(len(sig2))])

# sm.tsa.stattools.ccf(sig1, sig2, adjusted=False)

print(len(sig1))

corr = ax[1].xcorr(sig1, sig2, usevlines=True, normed=True, lw=2)

print(corr)

# ax[1].plot(np.arange(-10.0, 1, 1), corr[1], color='g')
# ax[1].set_xlim(-12, 12)

plt.show()