#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:49:49 2022

@author: antoiovi
"""

 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")


g=sns.relplot(    data=fmri, x="timepoint", y="signal", col="region",    hue="event", style="event", kind="line",)
g
g.axes
g.axes.size

#==================================================
fg = sns.FacetGrid(fmri, hue='event', col='region')
fg.map(sns.lineplot, data=fmri,x='timepoint',  y='signal', label='Signal')

# fg.figure : restituisce matplotli Figure
plt.show()

