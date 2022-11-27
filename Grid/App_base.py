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
       
        for i in range(1,5):
            ttk.Label(self,text="  Etichetta "+str(i)).grid(column=i,row=0,sticky='we')
        for i in range(1,3):
            ttk.Label(self,text="  Etichetta "+str(i)).grid(column=i,row=2,sticky='se')
 

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x400')
    root.title("Frame UNO")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()