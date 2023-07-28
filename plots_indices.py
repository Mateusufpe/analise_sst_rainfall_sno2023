# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:18:30 2023

@author: mateus
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = 'Dipolo'

df = pd.read_csv('APAC-GMMC-NOPE.csv', sep=';')
df['Data'] = pd.to_datetime(df['Data'])

fig, ax = plt.subplots(figsize=(20,5))
ax.plot(df['Data'], df[fileName])

plt.title(fileName)
plt.xlabel('Meses do ano')
plt.ylabel('Indice')

plt.ylim(-4.5, 4.5)

plt.savefig('SST' + fileName + '.png', dpi = 300, format='png', bbox_inches="tight")
