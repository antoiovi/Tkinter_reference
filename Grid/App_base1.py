#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk


class MainApplication(tk.Frame):
 
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
       
        fA= tk.Frame(self,  width=10, height=50)
        fB= tk.Frame(self, width=10, height=100)
        fA.pack(side='top')
        fB.pack(side='top',expand=True)
        
        f1 = tk.Frame(fA, background="bisque", width=100, height=100)
        f2 = tk.Frame(fA, background="pink", width=100, height=100)
        f1.grid(row=0, column=0, sticky="nsew")
        f2.grid(row=0, column=1, sticky="nsew")
        fA.grid_columnconfigure(0, weight=0)
        fA.grid_columnconfigure(1, weight=2)
        
        
        f3 = tk.Frame(fB, background="red", width=100, height=100)
        f4 = tk.Frame(fB, background="blue", width=100, height=100)
        f3.grid(row=0, column=0, sticky="nsew")
        f4.grid(row=0, column=1, sticky="nsew")
        tk.Label(f3,text="s").pack(side='left')

        
        fB.grid_columnconfigure(0, weight=0)
        fB.grid_columnconfigure(1, weight=0)
        
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x450')
    root.title("Frame UNO")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()