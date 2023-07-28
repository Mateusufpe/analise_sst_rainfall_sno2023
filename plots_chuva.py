# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:18:30 2023

@author: mateus
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fileName = 'chuvaSERTAOSAOFRANCISCO'

df = pd.read_csv(fileName + '.csv', sep=';')
df['Data'] = pd.to_datetime(df['Data'])

fig, ax = plt.subplots(figsize=(20,5))
ax.bar(df['Data'], df['mon_pluviometrico_hist_chuva_mm'], width=25)

plt.title(fileName)
plt.xlabel('Meses do ano')
plt.ylabel('Chuva (mm)')

# plt.ylim(0, 340)

plt.savefig('chuva_agreste' + fileName + '.png', dpi = 300, format='png', bbox_inches="tight")
