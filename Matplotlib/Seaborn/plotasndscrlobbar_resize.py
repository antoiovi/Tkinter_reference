#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:25:55 2022

@author: antoiovi
https://stackoverflow.com/questions/63061101/scrollbars-for-matplotlib-figure-in-tkinter



matplotlib figures are canvases. 
Therfore, its container frame won't resize to it, and bbox("all") won't work.
 Instead, we have to update the matplotlib canvas size to match the figure size
 and the toplevel canvas scrollregion to the figure size.


OKOKOK  Ok Ok Ok Ok 

"""

import os

from PIL import Image

import tkinter as tk
from tkinter import ttk, filedialog

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy as np

from functools import partial

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
        When the widget view is modified, 
        the widget notifies the scrollbar by calling the set method. 
        And when the user manipulates the scrollbar, 
        the widget’s yview method is called with the appropriate arguments.
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
            '''
            The call method is the interface to this underlying tcl interpreter.
            It allows you to construct a tcl command and ask the interpreter 
            to run it. It is a bridge between python and tcl.

            It is not typically used in application-level code, 
            though it can be useful in the rare cases where the Tkinter 
            wrapper around tcl/tk doesn't provide access to some feature 
            supported by tcl/tk
            '''
            self.tk.call('grid',
                         'remove',
                         self)
        else:
            self.grid()
        ttk.Scrollbar.set(self,
                          low,
                          high)

class DoubleScrollbarFrame(ttk.Frame):

    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''
        When the widget view is modified, 
        the widget notifies the scrollbar by calling the set method. 
        And when the user manipulates the scrollbar, 
        the widget’s yview method is called with the appropriate arguments.
        '''
        self.parent = parent

        super().__init__(self.parent,
                         *args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.canvas = tk.Canvas(self)
        self.frame = ttk.Frame(self.canvas)
        self.scroll_x = AutoScrollbar(self,
                                      orient = tk.HORIZONTAL)
        self.scroll_y = AutoScrollbar(self,
                                      orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        
        self.canvas.config(xscrollcommand = self.scroll_x.set,
                           yscrollcommand = self.scroll_y.set)
        
        '''
         And when the user manipulates the scrollbar, 
         the widget’s yview method is called with the appropriate arguments.
         '''
        self.scroll_x.config(command = self.canvas.xview)
        self.scroll_y.config(command = self.canvas.yview)
        
        self.canvas.create_window((0,0),
                                  window = self.frame,
                                  anchor = 'nw')
        
        self.frame.bind('<Configure>',
                        self.set_scrollregion)

    def position_widgets(self,
                         **kwargs):
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

        self.sizegrip.grid(row = 1,
                           column = 1,
                           sticky = 'se')

        #NOTE: Do not use geometry manager with `self.frame`. This will
        # pass control from the canvas to grid and the canvas will then
        # no longer know how much to grow.
        
    def set_scrollregion(self,
                         event):
        '''
        '''
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))

class Graph(ttk.Frame):

    def __init__(self,
                 parent,
                 axis_off = True,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent
        self.axis_off = axis_off

        super().__init__(self.parent,
                         *args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    
    def create_widgets(self,aspect=2,height=2):
        '''
        '''
   
        print("Crea facet grid")
        fg=sns.relplot(  data=fmri, x="timepoint", y="signal" , aspect=aspect,height=height,col="region",  hue="event", style="event", kind="line",)
      
        self.figure =fg.figure
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
        self.rowconfigure(0,weigh=1)

    def replot_graph(self,
                   aspect=1,height=2):
        '''
        '''
        self.axis.clear()
        self.frame.destroy()
        print("CREO WIDGET")
        self.create_widgets(aspect=aspect,height=height)
        print("POSIZIONO WIDGETS")
        self.position_widgets()
        self.mpl_canvas.draw()
        self.canvas.update()
        return
    def resize_plot(self, aspect=1,height=2):
        '''
        '''
        self.axis.clear()
        self.frame.destroy()
        print("CREO WIDGET")
        self.create_widgets(aspect=aspect,height=height)
        print("POSIZIONO WIDGETS")
        self.position_widgets()
        self.mpl_canvas.draw()
        self.canvas.update()
        return
        return
        


class Loader(ttk.Frame):
    '''
    '''
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

        #Set widgets to fill main window such that they are
        #all the same size
        self.aspecVar=tk.IntVar()
        self.aspecVar.set(3)
        self.heightVar=tk.IntVar()
        self.heightVar.set(1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.menuframe=ttk.Frame(self)
        input_label = ttk.Label(self.menuframe,  text = 'Input')
        input_label.pack(side='left')
        sp = ttk.Spinbox(self.menuframe, from_= 1, to = 20, textvariable=self.aspecVar)
        sp.pack()
        sp2 = ttk.Spinbox(self.menuframe, from_= 1, to = 20, textvariable=self.heightVar)
        sp2.pack()
        input_ok_button = ttk.Button(self.menuframe,    text = 'OK',command=self.reset_aspect).pack()

        
        self.graph = Graph(self)
        self.menuframe.grid(column=0,row=0,sticky='w')
        self.graph.grid(row = 1,
                        column = 0,
                        sticky = 'nsew')

 
        self.graph.replot_graph()

    def reset_aspect(self):
        self.graph.resize_plot(aspect=self.aspecVar.get(),height=self.heightVar.get())



class MainApp(tk.Tk):

    def __init__(self,
                 title,
                 *args,
                 **kwargs):
        '''
        '''
        self._title = title

        super().__init__(*args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #Set window title
        self.title(self._title)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.loader = Loader(self)

    def position_widgets(self):
        '''
        '''
        self.loader.grid(row = 0,
                         column = 0,
                         sticky = 'nsew')

if __name__ == '__main__':

    #Create GUI
    root = MainApp('MainApp')

    #Run program
    root.mainloop()