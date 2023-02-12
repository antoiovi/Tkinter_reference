#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:39:53 2022

@author: antoiovi
"""



import tkinter as tk
from tkinter import  ttk


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

import numpy as np
import pandas as pd
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
    def __init__(self, parent,df=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_figure(df)
        self.create_widgets()
        self.position_widgets()

    def create_figure(self,df=None,subplots=False):
        if df is None:
            self.figure = Figure(figsize=(5, 4), dpi=100)
            t = np.arange(0, 3, .01)
            ax = self.figure.add_subplot()
            line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
            ax.set_xlabel("time [s]")
            ax.set_ylabel("f(t)") 
        else:
            if subplots==True:
                self.figure = Figure(figsize=(8, 6), dpi=100)
                ax = self.figure.add_subplot()
    
                for name, values in df.iteritems():
                    print("Name -->",name)
                    x = values.index
                    line, = ax.plot(x,values,label=name)
                    ax.set_xlabel("Date")
                    ax.set_ylabel('Open')
                ax.legend()
            else:
                self.figure = Figure(figsize=(8, 6), dpi=100)
                k=1
                for name, values in df.iteritems():
                    # (nrows, ncols, index).
                    ax = self.figure.add_subplot(k,1,k)
                    print("Name -->",name)
                    x = values.index
                    line, = ax.plot(x,values,label=name)
                    ax.set_xlabel("Date")
                    ax.set_ylabel('Open')
                    k=k+1
                    ax.legend()
                    ax.change_geometry(2, 1, 1)
                

    def create_widgets(self):
        '''
        '''
        self.axis = self.figure.axes[0]

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
class Model:
    def __init__(self):
        try:
            aapl=pd.read_csv("../data/AAPL.csv")
            msft=pd.read_csv("../data/MSFT.csv")
            aapl['symbol']='AAPL'
            msft['symbol']='MSFT'
            
            frames = [aapl,msft]

        
            self.df=pd.concat(frames)
            self.df.reset_index(inplace=True)
            self.df['Simbolo']=self.df['symbol'].astype("category")

            print(self.df.head(5))
        except :
            self.df=None
            print("../dataframe is none")
    def group_by_symbol(self):
        return self.df.pivot(index='Date',columns=('symbol'),values='Open')

 
class Controller:
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root=tk.Tk()
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.model=Model()
        self.create_widgets()
        self.position_widgets()
        self.root.mainloop()
        
     def create_widgets(self):
        self.container=tk.Frame(self.root)
        self.container.columnconfigure(0,weight=1)
        self.container.rowconfigure(0,weight=1)
        
        self.frame_plot=FramePlot(self.container,self.model.group_by_symbol())
    
     def position_widgets(self):
         self.container.grid(column=0,row=0,sticky='news')
         self.frame_plot.grid(column=0,row=0,sticky='news')


# model=Model()
# model.df.columns

# model.df.groupby('symbol')

# d=model.df.pivot(index='Date',columns=('symbol'),values='Open')
# for name, values in d.iteritems():
#   print(values)

if __name__ == '__main__':
    Controller()