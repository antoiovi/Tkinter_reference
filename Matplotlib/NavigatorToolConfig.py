#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:49:38 2022

@author: antoiovi
https://stackoverflow.com/questions/59155873/how-to-remove-toolbar-button-from-navigationtoolbar2tk-figurecanvastkagg
"""



import tkinter as tk
from tkinter import BOTH, ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class FramePlot(tk.Frame):
    def _quit(self):
        print("quit ")
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        container=tk.Frame(self)

        container.grid(column=0, row=0)
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        ax = fig.add_subplot()
        self.line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        self.figura=fig
        #ax=fig.add_subplot(111)
        
        self.asse=ax
        
        self.canvas = FigureCanvasTkAgg(fig, master=container)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=5)
        
        '''   CLICK ON THE PLOT'''
        self.canvas.mpl_connect('button_press_event', self.click_on_plot)
        ''' MOVE ON THE PLOT'''
        self.canvas.mpl_connect('motion_notify_event', self.move_on_plot)

        
        NavigationToolbar2Tk.toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                                  t[0] not in ('Home','Pan','Forward','Back','Zoom','Subplots')]        
        toolbar = NavigationToolbar2Tk(self.canvas, container,  pack_toolbar=False)
        print(toolbar.toolitems)  
        '''
        (('Home', 'Reset original view', 'home', 'home'), 
         ('Back', 'Back to previous view', 'back', 'back'), 
         ('Forward', 'Forward to next view', 'forward', 'forward'), 
         (None, None, None, None), 
         ('Pan', 'Left button pans, Right button zooms\nx/y fixes axis, CTRL fixes aspect', 'move', 'pan'), 
         ('Zoom', 'Zoom to rectangle\nx/y fixes axis', 'zoom_to_rect', 'zoom'),
         ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'), 
         (None, None, None, None),
         ('Save', 'Save the figure', 'filesave', 'save_figure'))
        '''
        
        button = tk.Button(master=toolbar, text="Quit", command=self._quit)
        #button.pack()
        button.pack(side="left")

        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.x=1
        frameButtons=tk.Frame(container)
        ttk.Button(frameButtons,text="--  +1 --",command=self.update).pack(side=tk.LEFT)
        
        slider_update = tk.Scale(container, from_=1, to=5, orient=tk.HORIZONTAL,
                                 command=self.update_frequency, label="Frequency [Hz]")
        
        toolbar.pack(side=tk.LEFT)
        frameButtons.pack(side=tk.BOTTOM)
        slider_update.pack(side=tk.BOTTOM)

    def click_on_plot(self,event):
        print("CLICK ON PLOT ",event)
        
    def move_on_plot(self,event):
        return
        print("MOVE ON TH EPLOT ",event)
 
    def update(self):
            self.x=self.x+1 if self.x<5 else 1
            new_val=self.x
            t = np.arange(0, 3, .01)
            # retrieve frequency
            f = float(new_val)
            # update data
            y = 2 * np.sin(2 * np.pi * f * t)
            self.line.set_data(t, y)
            # required to update canvas and attached toolbar!
            self.canvas.draw()
            return
    def update_frequency(self,new_val):
            # retrieve frequency
            f = float(new_val)
            t = np.arange(0, 3, .01)
            # update data
            y = 2 * np.sin(2 * np.pi * f * t)
            self.line.set_data(t, y)
            # required to update canvas and attached toolbar!
            self.canvas.draw()


class Statusbar(tk.Frame):
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.messagelbl=ttk.Label(self, text="Status bar")
        self.messagelbl.grid(column=0, row=0)
        

        
   
class MainApplication(tk.Frame):

        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        framePlot=FramePlot(self)        
        framePlot.grid(column=1,row=1,sticky='nwes',padx=5,pady=5)

        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='S',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=0)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matplotlib plott in tkinter frame")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()