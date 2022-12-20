#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""

import tkinter as tk
from tkinter import  ttk,Tk,Toplevel
import seaborn as sns

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure


# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")

class Navigationbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        ttk.Label(self, text="Navigation bar").grid(column=0, row=0,)
        ttk.Button(self,text="Button").grid(column=1,row=0)



class Plotting_area(tk.Frame):
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        container=tk.Frame(self)
        self.canvas=self.init_gui()

     def init_gui(self) -> FigureCanvasTkAgg:
        # create empty figure and draw
        init_figure = self.create_figure()
        canvas = FigureCanvasTkAgg(init_figure, master=self)
        canvas.draw()
        hbar=tk.Scrollbar(self,orient=tk.HORIZONTAL)
        vbar=tk.Scrollbar(self,orient=tk.VERTICAL)
        canvas.get_tk_widget().config(bg='#FFFFFF',scrollregion=(0,0,500,500))
        
        
        canvas.get_tk_widget().config(width=400,height=450)
        canvas.get_tk_widget().config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)


         # AGGIUNGO IL TOOLBAR AL CANVAS
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        # PACKING 
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        hbar.pack(side = tk.BOTTOM, fill=tk.X)
        hbar.config(command=canvas.get_tk_widget().xview)
        
        vbar.pack(side = tk.RIGHT, fill=tk.Y)
        vbar.config(command=canvas.get_tk_widget().yview)
        canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.X,expand = True)

        
        toolbar.pack(side=tk.TOP)

        return canvas
    
     def create_figure(self) -> Figure:
         # plot the data
        figure = Figure(figsize=(6, 6))
        ax = figure.subplots()
        # Plot the responses for different events and regions
        sns.lineplot(x="timepoint", y="signal",
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
        Navigationbar(self).pack(side='top')
        Plotting_area(self).pack(side='top')

   
class Testseaborn():  # The Controller
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.withdraw()
        root = Tk()
        root.title("Frame UNO")
        #content=tk.Frame(root,bg='green')
        #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
        root.geometry('500x400')
        View(root).grid(column=0,row=0)
        root.mainloop()


if __name__ == '__main__':
    Testseaborn()#.mainloop()