#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width


class Navigationbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        ttk.Label(self, text="Navigation bar").grid(column=0, row=0,)
        ttk.Button(self,text="Button").grid(column=1,row=0)


class Statusbar(tk.Frame):
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.messagelbl=ttk.Label(self, text="Status bar")
        self.messagelbl.grid(column=0, row=0)

     def update(self,program_event):
        return
        
   
class MainApplication(tk.Frame):
    x=0
    def button1_click(self):
        s=str(self.x)
        self.label1.config(text=s)
        self.x=self.x+1
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #self.title("Frame UNO")
        #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
        #self.geometry('1000x800')
        button1=ttk.Button(self,text="Bottone 1",command=self.button1_click)
        button1.grid(column=0,row=0,sticky='w')
        self.label1=ttk.Label(self,text="Etichetta 1")
        self.label1.grid(column=1,row=0,sticky='w')
        
        
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='NWES',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame UNO")
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