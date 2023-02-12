#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:19:39 2023

@author: antoiovi
"""


import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
import os

f1="/home/antoiovi/Tkinter_reference/data/AAPL.csv"
f2="/home/antoiovi/Tkinter_reference/data/MSFT.csv"

aapl=pd.read_csv(f1)
msft=pd.read_csv(f2)
aapl['symbol']='AAPL'
msft['symbol']='MSFT'

frames = [aapl,msft]


df=pd.concat(frames)

df.reset_index(inplace=True)
df['Simbolo']=df['symbol'].astype("category")
df[df['symbol']=='MSFT']
df[df['symbol']=='AAPL']

print(df.head(5))

fig, ax = plt.subplots()

ax.plot(aapl['Date'],aapl['Open'])
plt.show()



#=======================================================================

dt = 1.0
t = np.arange(0, 10, dt)
s1 =3*t
s1[4]=None
fig, ax = plt.subplots()
ax.plot(t, s1)
plt.show()

#------------------------------------------------------------------------

fig, ax = plt.subplots()
df
a=df[df['symbol']=='AAPL']
b=df[df['symbol']=='MSFT']
b
a
#data=df[df['symbol']=='AAPL']
data=df
data.set_index('Date',inplace=True)

data.head(3)

a
fg = sns.FacetGrid(data,hue='symbol',col='symbol')

fg.axes[0][0].plot(a.index,a['Open'])
fg.axes[0][1].plot(b.index, b['Open'])



plt.show()
a
