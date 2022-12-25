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

#Matplotlib Default DPI
DEFAULT_DPI = 100

#Matplotlib Default PPI
DEFAULT_PPI = 72

class AutoScrollbar(ttk.Scrollbar):

    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent

        super().__init__(self.parent,
                         *args,
                        **kwargs)

    def set(self,
            low,
            high):
        '''
            When the widget view is modified,
            the widget notifies the scrollbar by calling the set method.
            
        '''
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.tk.call('grid',
                         'remove',
                         self)
        else:
            self.grid()
        ttk.Scrollbar.set(self,
                          low,
                          high)
class FramePlot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.figure = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        ax = self.figure.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")  
            
      
        size = self.figure.get_size_inches()*self.figure.dpi # size in pixels
        print("SIZE>>>",size)
        self.axis = self.figure.axes[0]

        #if self.axis_off:
        #    self.axis.set_axis_off()

        self.canvas = tk.Canvas(self)
        self.frame = ttk.Frame(self.canvas)

        self.mpl_canvas = FigureCanvasTkAgg(self.figure,
                                            self.frame)

        self.mpl_canvas.draw()

        self.scroll_x = AutoScrollbar(self,
                                      orient = tk.HORIZONTAL)
        self.scroll_y = AutoScrollbar(self,
                                      orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        
        self.canvas.config(xscrollcommand = self.scroll_x.set,
                           yscrollcommand = self.scroll_y.set)
        self.scroll_x.config(command = self.canvas.xview)
        self.scroll_y.config(command = self.canvas.yview)
        
        self.cwid = self.canvas.create_window((0,0),
                                              window = self.frame,
                                              anchor = 'nw')

        self.frame.bind('<Configure>',
                        self.set_scrollregion)

        self.toolbar_frame = ttk.Frame(self)

        self.toolbar = NavigationToolbar2Tk(self.mpl_canvas,
                                            self.toolbar_frame)

    def set_scrollregion(self,
                         event):
        '''
        '''
        w, h = self.figure.get_size_inches()
        #print("Scroll region",w,h)
        w = int(w * DEFAULT_DPI)
        h = int(h * DEFAULT_DPI)
        scrollregion = (0,0,w,h)
        
        self.canvas.configure(scrollregion = scrollregion)
        
    def position_widgets(self):
        '''
        '''
        self.scroll_x.grid(row = 1,
                           column = 0,
                           sticky = 'ew')

        self.scroll_y.grid(row = 0,
                           column = 1,
                           sticky = 'ns')

        self.canvas.grid(row = 0,
                         column = 0,
                         sticky = 'nsew')

        self.mpl_canvas.get_tk_widget().grid(row = 0,
                                             column = 0,
                                             sticky = 'nsew')

        self.sizegrip.grid(row = 1,
                           column = 1,
                           sticky = 'se')

        #NOTE: Do not use geometry manager with `self.frame`. This will
        # pass control from the canvas to grid and the canvas will then
        # no longer know how much to grow.

        self.toolbar.update()
        self.toolbar_frame.grid(row = 2,
                                column = 0,
                                sticky = 'sew')        
  




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