#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 20:25:58 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk


class Frame1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        ttk.Label(self, text="Navigation bar").grid(column=0, row=0,)
        ttk.Button(self,text="Button").grid(column=1,row=0)


class MainApplication(tk.Frame):
 
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
       
        for i in range(1,5):
            ttk.Label(self,text="  Etichetta "+str(i)).grid(column=i,row=0,sticky='we')
        for i in range(1,3):
            ttk.Label(self,text="  Etichetta "+str(i)).grid(column=i,row=2,sticky='se')
        frame1=Frame1(self,background='yellow').grid(column=0,row=3,sticky='w')
        frame2=Frame1(self,background='green').grid(column=1,row=3,sticky='e')

 

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x400')
    root.title("Frame UNO")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()