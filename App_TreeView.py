#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width


class FrameTreeView(tk.Frame):
    initial_data=[ ["Ant","Iov","01-01-2000",4], 
                  ["Mary","Bal","31-01-1987",7],
                  ["Bob","Crown","27-02-1995",25],
                  ["Tony","Hair","31-10-2001",450],
                  ["July","Benson","02-07-1970",7.3],
                  ]
    
    def init_Treewview(self):
        self.delete_all()
        i=0
        for r in self.initial_data:
            self.treeDf.insert('','end',iid=i,text='---',values=r) 
            i=i+1
        return
    
    
    def alternate_Colors(self):
        self.delete_all()
        i=0
        for r in self.initial_data:
            if i % 2 == 0:
                self.treeDf.insert("",'end', values=r,tag='blue')
            else:
                self.treeDf.insert("",'end', values=r,tag='gray')
            i=i+1
        self.treeDf.tag_configure('gray', background='#cccccc')
        self.treeDf.tag_configure('blue', background='#808080')
        return

    
    def delete_all(self):
        for i in self.treeDf.get_children():
            self.treeDf.delete(i)
        return
    
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.treeDf = ttk.Treeview(self, columns=() ,show='headings',selectmode='none')
        colonne=['FirstName','LastName','Date','Number']
        larghezza=[150,150,80,40]
        self.treeDf["columns"] =colonne
        i=0
        for c in colonne:
            self.treeDf.heading(i, text=c)
            self.treeDf.column(i, width=larghezza[i])
            i=i+1
        self.init_Treewview()
        self.treeDf.pack(side=tk.TOP,   fill=tk.BOTH,expand=True)
        ttk.Button(self,text="Delete",command=self.delete_all).pack(side=tk.LEFT)
        ttk.Button(self,text="Reset",command=self.init_Treewview).pack(side=tk.LEFT)
        ttk.Button(self,text="Alternative colors",command=self.alternate_Colors).pack(side=tk.LEFT)
        



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
        
        frameTreeviw=FrameTreeView(self)        
        frameTreeviw.grid(column=0,row=0)
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='NWES',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame Treeview test")
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