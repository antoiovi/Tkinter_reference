#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:51:50 2023

@author: https://stackoverflow.com/questions/51409295/multiprocess-plotting-in-matplotlib
https://stackoverflow.com/questions/16745507/tkinter-how-to-use-threads-to-preventing-main-event-loop-from-freezing
"""
import pandas as pd
import matplotlib.pyplot as plt

import multiprocessing
#multiprocessing.freeze_support() # <- may be required on windows

df = pd.DataFrame(data={'i':['A','A','B','B'],
                       'x':[1.,2.,3.,4.],
                       'y':[1.,2.,3.,4.]})
df.set_index('i', inplace=True)
df.sort_index(inplace=True)

# function which creates a figure from the data
def Draw(df, i):
    fig, ax  = plt.subplots()
    df = df.loc[i,:]
    ax.scatter(df['x'], df['y'])
    plt.show()

# creating figures in parallel
args = [(df,'A'), (df,'B')]

def multiP():
    for a in args:
        p = multiprocessing.Process(target=Draw, args=a)
        p.start()

if __name__ == "__main__":         
    multiP()