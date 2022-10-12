#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width


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
        t = np.arange(0, 30, .1)
        ax = fig.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        
        xmin,xmax = ax.get_xlim()

        ymin,ymax = ax.get_ylim()
        print("xmin,xmax ",xmin,xmax)
        print("ymin,ymax ",ymin,ymax)
        ax_h=ax.bbox.height
        ax_w =  ax.bbox.width
        print("Larghezza ed altezza  del plot H, W ",ax_h,ax_w)

        '''
            CREA UN CANVAS CON DENTRO LA Figure
        '''
        canvas = FigureCanvasTkAgg(fig, master=container)  # A tk.DrawingArea.
        # Render the Figure.
        canvas.draw()
        # AGGIUNGO IL TOOLBAR AL CANVAS
        # Funziona solo con pack
        toolbar = NavigationToolbar2Tk(canvas, container)
        toolbar.update()
        self.hbar=tk.Scrollbar(container,orient=tk.HORIZONTAL)
        self.vbar=tk.Scrollbar(container,orient=tk.VERTICAL)

        #canvas.get_tk_widget().config(bg='#FFFFFF',scrollregion=(0,0,ax_w+100,ax_h+100))
        canvas.get_tk_widget().config(bg='#FFFFFF',scrollregion=(0,0,ax_w+500,ax_h+100))
        # Queste righe cambiano la dimensione del grafico 
        # Imposto la larghezza del plot piu un margine per essere sicuro che venga disegnato tutto
        canvas.get_tk_widget().config(width=ax_w+100,height=ax_h+100)
        #canvas.get_tk_widget().config(width=ax_w+400,height=ax_h+100)
        canvas.get_tk_widget().config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        self.hbar.pack(side = tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=canvas.get_tk_widget().xview)
        
        self.vbar.pack(side = tk.RIGHT, fill=tk.Y)
        self.vbar.config(command=canvas.get_tk_widget().yview)
        canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.X,expand = True)



   
class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        framePlot=FramePlot(self)
        framePlot.grid(column=0,row=0,sticky='news')
        self.columnconfigure(0,weight=1)
        # self.rowconfigure(0,weight=0)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollbar on plot")
    content=tk.Frame(root,bg='green')
    #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
    root.geometry('500x400')
    # styck (NSEW) espande il content in tutta la root 
    content.grid(column=0,row=0,sticky='NWES') 
    # styck (NSEW) espande mainapplication nel content
    MainApplication(content).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    # Senza questa riga content non occupa tutto il frame root    
    content.columnconfigure(0,weight=1)
    content.rowconfigure(0,weight=1)
    # Senza questa riga root non occupa tutto il frame della applicazione    
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    #root.pack(   fill='x')
    root.mainloop()