#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi

https://tkdocs.com/shipman//dimensions.html
"""

import tkinter as tk
from tkinter import  ttk,Tk,Toplevel
import seaborn as sns

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

DEFAULT_DPI = 100

#Matplotlib Default PPI
DEFAULT_PPI = 72
# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")

class Navigationbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        ttk.Label(self, text="Navigation bar").grid(column=0, row=0,)
        ttk.Button(self,text="Button").grid(column=1,row=0)



class Plotting_area(tk.Frame):
     '''
     https://stackoverflow.com/questions/63061101/scrollbars-for-matplotlib-figure-in-tkinter
     matplotlib figures are canvases. 
    Therfore, its container frame won't resize to it, and bbox("all") won't work.
     Instead, we have to update the matplotlib canvas size to match the figure size
     and the toplevel canvas scrollregion to the figure size.
     '''
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
         # create empty figure and draw
        self.figure = self.create_figure()
        
        # 1 CREO UN CANVAS a cui saranno assegnati gli scroll bar
        self.canvas = tk.Canvas(self)
        
        # 2 CREO UN FRAME figlio di canvas che conterra il maptplot canvas
        self.frame = ttk.Frame(self.canvas)
        # 3 il matplotlib_canvas 'e contenuto in un frame
        self.mpl_canvas = FigureCanvasTkAgg(self.figure,
                                            self.frame)

        self.mpl_canvas.draw()
        self.sizegrip = ttk.Sizegrip(self)

        self.hbar=tk.Scrollbar(self,orient=tk.HORIZONTAL)
        self.vbar=tk.Scrollbar(self,orient=tk.VERTICAL)
        self.canvas.config(xscrollcommand = self.hbar.set,
                           yscrollcommand = self.vbar.set)
        self.hbar.config(command = self.canvas.xview)
        self.vbar.config(command = self.canvas.yview)
        
        # 4 Creare la window che contiene il frame che contiene il matplot_canvas
        self.cwid = self.canvas.create_window((0,0),
                                              window = self.frame,
                                              anchor = 'nw')

        self.frame.bind('<Configure>',
                        self.set_scrollregion)
        

        
 
        # PACKING 
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.hbar.pack(side = tk.BOTTOM, fill=tk.X)
        
        self.vbar.pack(side = tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.BOTTOM,fill=tk.BOTH,expand = True)
        self.mpl_canvas.get_tk_widget().grid(row = 0,
                                             column = 0,
                                             sticky = 'nsew')

    
     def set_scrollregion(self,
                         event):
        '''
        AdATTARE LA SCROLL REGION ALLA DIMENSIONE DELLA FIGURE
        '''

        w, h = self.figure.get_size_inches()
        #print("Scroll region",w,h)
        w = int(w * DEFAULT_DPI)
        h = int(h * DEFAULT_DPI)
        scrollregion = (0,0,w,h)
        self.canvas.configure(scrollregion = scrollregion)
        
     def create_figure(self) -> Figure:
         # plot the data
        figure = Figure(figsize=(6, 6))
        ax = figure.subplots()
        # Plot the responses for different events and regions
        fg=sns.lineplot(x="timepoint", y="signal",
                hue="region", style="event",
                data=fmri,ax=ax)
        return figure
    
     def redraw_figure(self):
        figure = self.create_figure()
        self.canvas.figure = figure
        self.canvas.draw()
        
 
class View(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #self.protocol('WM_DELETE_WINDOW', master.destroy)
        nb=Navigationbar(self)
        self.plotarea=Plotting_area(self)
        nb.pack(side='top')
        self.plotarea.pack(side='top',expand=True,fill='both')
        
class Testseaborn():  # The Controller
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.withdraw()
        root = Tk()
        root.title("Frame UNO")
        #content=tk.Frame(root,bg='green')
        #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
        root.geometry('500x400')
        View(root).grid(column=0,row=0,sticky='nwes')
        root.columnconfigure(0,weight=1)

        root.mainloop()


if __name__ == '__main__':
    Testseaborn()#.mainloop()