# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:09:59 2023

@author: LOFEC-AIRMOD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from statsmodels.tsa.tsatools import detrend

def climatology(df):
        
    result = []
    monCount = []
    
    for i in range(1, 13): 
        result.append(0)
        monCount.append(0)
        
    for l in df.index:
        date = df.at[l, 'Data']
        
        if np.isnan(df.at[l, 'mon_pluviometrico_hist_chuva_mm']) == False:
            result[date.month - 1] = result[date.month - 1] + df.at[l, 'mon_pluviometrico_hist_chuva_mm']

            monCount[date.month - 1] = monCount[date.month - 1] + 1

    #print(result)

    for c in range(1, 13):
        result[c - 1] = result[c - 1]/monCount[c - 1]
    
    
    #print(monCount)
    
    return result

def anomaly(df, cl):
    
    an = []
    
    for l in df.index:
        date = df.at[l, 'Data']
        
        an.append(df.at[l, 'mon_pluviometrico_hist_chuva_mm'] - cl[date.month - 1])
    
    return an

def plotclimatology(clim, fileName):
    
    m = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    fig, ax = plt.subplots(figsize=(10,8))
    ax.bar(m, clim)

    plt.title('Climatologia mensal de Chuvas ' + fileName)
    plt.xlabel('Meses do ano')
    plt.ylabel('Chuva (mm)')

    plt.ylim(0, 340)
    
    fileName = str(fileName)
    plt.savefig('Climatologia_mensal_chuva_' + fileName + '.png', dpi = 300, format='png', bbox_inches="tight")

df = pd.read_csv('chuvaSERTAOSAOFRANCISCO.csv', sep=';')
df['Data'] = pd.to_datetime(df['Data'])

#CLIMATOLOGIA

climResult = climatology(df)

plotclimatology(climResult, 'SERTAOFRANCISCO')

#ANOMALIA

ann = anomaly(df, climResult)
an = pd.DataFrame(anomaly(df, climResult))

an1 = detrend(an[0]);

an2 = signal.detrend(df['mon_pluviometrico_hist_chuva_mm'])

print(pd.DataFrame(an1)[0].corr(pd.DataFrame(an2)[0], method='spearman'))

colormat=np.where(an2>0, 'b','r')

fig, ax = plt.subplots(figsize=(20, 5))

ax.bar(df['Data'], an2, width=20,color=colormat)

plt.title('Anomalia de Chuvas mensais RMR Detrend')
plt.xlabel('Tempo')
plt.ylabel('Chuva (mm)')



plt.savefig('Anomalia_mensal_chuvas_RMR_teste.png', dpi = 300, format='png', bbox_inches="tight")


plt.show()