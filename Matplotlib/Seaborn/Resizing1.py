#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""
from typing import Callable

import tkinter as tk
from tkinter import BOTH, ttk,Tk
from turtle import width
import numpy as np
import seaborn as sns
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
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
        Plotting_area(self).pack(side='left')

   
class Testseaborn(Tk):  # The Controller
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()
        root = Tk()
        root.title("Frame UNO")
        content=tk.Frame(root,bg='green')
        #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
        root.geometry('500x400')
        View(root).grid(column=0,row=0)



if __name__ == '__main__':
    Testseaborn().mainloop()