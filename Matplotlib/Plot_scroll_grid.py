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
        t = np.arange(0, 3, .01)
        ax = fig.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
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
        #  TclError: cannot use geometry manager grid inside
        #       .!frame.!mainapplication.!frameplot.!frame which already has slaves managed by pack
        #toolbar = NavigationToolbar2Tk(canvas, container)
        #toolbar.update()
        self.hbar=tk.Scrollbar(container,orient=tk.HORIZONTAL)
        self.vbar=tk.Scrollbar(container,orient=tk.VERTICAL)

        canvas.get_tk_widget().config(bg='#FFFFFF',scrollregion=(0,0,500,500))
        #canvas.get_tk_widget().config(width=500,height=300)
        # Queste righe cambiano la dimensione del grafico 
        # Imposto la larghezza del plot piu un margine per essere sicuro che venga disegnato tutto

        canvas.get_tk_widget().config(width=ax_w+100,height=ax_h+100)
        canvas.get_tk_widget().config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        
        canvas.get_tk_widget().grid(row=0, column=0, sticky="WENS")

        self.hbar.grid(row=1, column=0, sticky="WE")
        self.hbar.config(command=canvas.get_tk_widget().xview)
        self.vbar.grid(row=0, column=1, sticky="NS")
        self.vbar.config(command=canvas.get_tk_widget().yview)




class Statusbar(tk.Frame):
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.messagelbl=ttk.Label(self, text="Status bar")
        self.messagelbl.grid(column=0, row=0)
        
   
class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        framePlot=FramePlot(self)
        framePlot.grid(column=0,row=0,sticky='news')
        
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='NWES',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)


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