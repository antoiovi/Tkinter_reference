#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi



Reference : 
    https://tkdocs.com/tutorial/tree.html
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Treeview.html
    
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width
import pandas as pd

class FrameTreeView(tk.Frame):
    def get_df(self):
        data={'firstname':["Anto","Bob","Cindy","Denny"],'lastname':["Arc","Brick","Cook","Drill"],'age':[40,22,35,28]}
        return  pd.DataFrame(data)

    def set_TreeViewdata_o(self,df):
        if isinstance(df, pd.core.frame.DataFrame):
            # Delete all data from treeview
            for i in self.treeview.get_children():
                 self.treeview.delete(i)
            for i,r in df.iterrows():
                 val=list(r)
                 self.treeview.insert("",'end', values=val)
            return
    
    def set_TreeViewdata(self,df):
        if isinstance(df, pd.core.frame.DataFrame):
            # Delete all data from treeview
            for i in self.treeview.get_children():
                 self.treeview.delete(i)
            for i,r in df.iterrows():
                 val=list(r)
                 self.treeview.insert("",'end', values=val,tags=('ttk'))
            
            self.treeview.tag_bind('ttk', '<1>', self.itemClicked)  
            return
    




    
    def print_TreeViewdata(self):
        print("Print tree view lines :")
        for line in self.treeview.get_children():
                print(self.treeview.item(line)['values'])
        selected=self.treeview.focus()
        print(" Selected iid = ",selected," value -->",self.treeview.item(selected)['values'])
    
    def append_TreeViewdata(self,df):
        if isinstance(df, pd.core.frame.DataFrame):
            for i,r in df.iterrows():
                 val=list(r)
                 self.treeview.insert("",'end', values=val,tags=('ttk'))
            self.treeview.tag_bind('ttk', '<1>', self.itemClicked)  
            return

    
    
    def alternate_Colors(self):
        # TODO
        return

    
    def delete_all(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        return
    


    def itemClicked(self,event):
        '''
         This evente is binded whe insert elements in def set_TreeViewdata(self,df)...

             treeview.insert("",'end', values=val,tags=('ttk'))
             treeview.tag_bind('ttk', '<1>', self.itemClicked)  
 
        '''
        # This returns the lost item
        iid=self.treeview.focus()
        print(" Lost focus  iid = ",iid," value -->",self.treeview.item(iid)['values'])
        # Identify the row at point (x,y)
        rowID = self.treeview.identify('item', event.x, event.y)
        if rowID:
            self.treeview.selection_set(rowID) # Selection at point clicked
            self.treeview.focus_set()
            self.treeview.focus(rowID)
            print(" Selected iid = ",rowID," value -->",self.treeview.item(rowID)['values'])
        return

    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        '''
            selectmode='browse'	The user may select only one item at a time.
            selectmode='extended'	The user may select multiple items at once.
            selectmode='none'	The user cannot select items with the mouse.
        '''            
        self.treeview = ttk.Treeview(self, columns=() ,show='headings',selectmode='browse')
        
        df=self.get_df()
        col_names=['FirstName','LastName','Age']
        col_widths=[150,150,40]
        self.treeview["columns"] =col_names
        i=0
        for c in col_names:
            self.treeview.heading(i, text=c)
            self.treeview.column(i, width=col_widths[i])
            i=i+1

        self.treeview.pack(side=tk.TOP,   fill=tk.BOTH,expand=True)
        ttk.Button(self,text="Delete",command=self.delete_all).pack(side=tk.LEFT)
        ttk.Button(self,text="Set Data",command= lambda: self.set_TreeViewdata(df)).pack(side=tk.LEFT)
        ttk.Button(self,text="Append Data",command= lambda: self.append_TreeViewdata(df)).pack(side=tk.LEFT)
        ttk.Button(self,text="Print Data",command=self.print_TreeViewdata).pack(side=tk.LEFT)
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