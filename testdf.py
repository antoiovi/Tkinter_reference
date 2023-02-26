#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:44:03 2023

@author: antoiovi
"""

import pandas as pd

f="data/enviromental.csv"
df=pd.read_csv(f,sep=',',decimal='.')
df.columns
df.dtypes


df1 = df.groupby(['station','sensor'], as_index=False).sum(min_count=1)


x={'a':[1,None,3,4],'b':[1,1,2,2]}
df=pd.DataFrame(x)
df.groupby('b')['a'].mean()

df.groupby('b')['a'].mean(min_count=2)

df.groupby('b')['a'].sum()
df.groupby('b')['a'].sum(min_count=2)

