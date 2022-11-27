#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
https://tkdocs.com/tutorial/grid.html#resize

Modificare nella riga 120
       self.columnconfigure(0,weight=0)
      OPPURE
      self.columnconfigure(0,weight=1)
      
      se metto weight=1 il frame con il plot si espande e contrae
      se metto weigth=0 il frame con il plot viene nascosto dal frame adiacente
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width


from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure

import numpy as np

class ReportNotes(tk.Frame):
            
    def set_message(self,message):
        self.text_box.config(state='normal')
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, message)
        self.text_box.config(state='disabled')

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  width=100, height=60,*args, **kwargs)
        
        self.text_box = tk.Text(self)
        ys = ttk.Scrollbar(self, orient = 'vertical', command = self.text_box.yview)
        xs = ttk.Scrollbar(self, orient = 'horizontal', command = self.text_box.xview)
        self.text_box['yscrollcommand'] = ys.set
        self.text_box['xscrollcommand'] = xs.set
        self.text_box.insert('end', ".......\n...\n...")
        self.text_box.grid(column = 0, row = 0, sticky = 'nwes')
        xs.grid(column = 0, row = 1, sticky = 'we')
        ys.grid(column = 1, row = 0, sticky = 'ns')
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_propagate(False)
        
        
class FramePlot(tk.Frame):
    x=0
    def button1_click(self):
        self.x=self.x+1
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs,bg='red')
        container=tk.Frame(self)
        container.grid(column=0, row=0,sticky='news')
        button1=ttk.Button(self,text="Bottone 1",command=self.button1_click)
        #button1.grid(column=1,row=0,sticky='we')
        self.columnconfigure(0,weight=2)
        fig = Figure(figsize=(4, 4))
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
        canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand = True)
        


   
class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        framePlot=FramePlot(self)
        framePlot.grid(column=0,row=0,sticky='news')
        report=ReportNotes(self)
        report.grid(column=1,row=0,sticky='news')
        # Se metto weight =1 a colonna 0, il frame con il plot si espande e contrae
        #   contraendo e espandendo il grafico, quindi bisogna metter weight=0
        #self.columnconfigure(0,weight=0)
        self.columnconfigure(0,weight=0)
        self.columnconfigure(1,weight=1)
    





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrollbar on plot")
    content=tk.Frame(root,bg='green')
    #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
    root.geometry('1000x400')
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