#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

import numpy as np

class FramePlot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        container=tk.Frame(self)
        container.grid(column=0, row=0)
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        ax = fig.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        '''
            CREA UN CANVAS CON DENTRO LA Figure
        '''
        canvas = FigureCanvasTkAgg(fig, master=container)  # A tk.DrawingArea.
        # Render the Figure.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=5)
        
        # AGGIUNGO IL TOOLBAR AL CANVAS
        toolbar = NavigationToolbar2Tk(canvas, container)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



        
   
class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        framePlot=FramePlot(self)        
        framePlot.grid(column=1,row=1,sticky='nwes',padx=5,pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matplotlib plott in tkinter frame")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()