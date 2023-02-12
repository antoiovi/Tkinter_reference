#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 20:59:56 2022

@author: antoiovi
"""

"""
Created on Fri Dec 23 21:25:55 2022

@author: antoiovi
https://stackoverflow.com/questions/63061101/scrollbars-for-matplotlib-figure-in-tkinter


effbot.org/tkinterbook (dead link )

"""


import tkinter as tk
from tkinter import ttk

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

class DoubleScrollbarFrame(ttk.Frame):

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
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
 
        self.canvas = tk.Canvas(self)
        self.frame = ttk.Frame(self.canvas)
        self.scroll_x = AutoScrollbar(self,
                                      orient = tk.HORIZONTAL)
        self.scroll_y = AutoScrollbar(self,
                                      orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        
        self.canvas.config(xscrollcommand = self.scroll_x.set,
                           yscrollcommand = self.scroll_y.set)
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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollbar pattern")
    root.geometry('500x400')
    # styck (NSEW) espande il content in tutta la root 
    AutoScrollbar(root).grid(column=0,row=0,sticky='NWES') 
  
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    #root.pack(   fill='x')
    root.mainloop()