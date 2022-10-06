#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 08:28:35 2022

@author: antoiovi
"""
import tkinter as tk
from tkinter import BOTH, ttk

import pandas as pd


'''   TREEVIW '''
class Tree_test(tk.Frame):
    
    def callback_selectFile(self):
         #Cancella tutti gli elementi da TREE
         self.treeDf.delete(*self.treeDf.get_children()) 
         dati=pd.DataFrame()
         dati.reset_index(inplace=True)
         iid=0
         for index,row in dati.iterrows():
             r=(row['station'], row['sensor'],row['Numero dati'],row['Dal'],row['Al'])
             # INSERISCI RIGA DEL DATAFRAME IN TREE
             self.treeDf.insert('','end',iid=iid,text='---',values=r) 
             iid=iid+1
         return
     
    def __init__(self, parent, *args, **kwargs):
         tk.Frame.__init__(self, parent, *args, **kwargs)    
         container = tk.Frame(self,bg='blue')
         self.treeDf = ttk.Treeview(container, columns=() ,show='headings',selectmode='none')
         colonne=['Stazione','Sensore','Numero dati','Dal','Al']
         larghezza=[250,250,100,100,100]
         self.treeDf["columns"] =colonne
         i=0
         for c in colonne:
             self.treeDf.heading(i, text=c)
             self.treeDf.column(i, width=larghezza[i])
             i=i+1
         self.treeDf.grid(column=0,row=1,sticky='wnse')
         container.grid(column=0,row=3,sticky='nswe')



class ReportDati(tk.Frame):

            
    def set_message(self,df):
        if isinstance(df, pd.core.frame.DataFrame):
            # CANCELLA IL COTENUTO DELLA TABELLA
            for i in self.treeDf.get_children():
                self.treeDf.delete(i)
            print("check oK")
            station0=" "
            station1=" "
            tags=['gray','white']
            x=0
            for i,r in df.iterrows():
                
                l=list(i)+list(r)
                station1=l[0]
                if station0==station1:
                    l[0]=" "
                else:
                    station0=l[0]
                    self.treeDf.insert("",'end', values=l,tag='blue')
                    x=1
                    continue
                x= 0 if x is 1  else 1
                self.treeDf.insert("",'end', values=l,tag=tags[x])
                print(tags[x])
            self.treeDf.tag_configure('gray', background='#cccccc')
            self.treeDf.tag_configure('blue', background='#808080')
            

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.treeDf = ttk.Treeview(self, columns=() ,show='headings',selectmode='none')
        
        colonne=['Stazione','Sensore','Numero dati','Dal','Al']
        larghezza=[250,250,80,80,80]
        self.treeDf["columns"] =colonne
        i=0
        for c in colonne:
            self.treeDf.heading(i, text=c)
            self.treeDf.column(i, width=larghezza[i])
            i=i+1
        self.treeDf.grid(column=0,row=1,sticky='wnse')
        
        ys = ttk.Scrollbar(self, orient = 'vertical', command = self.treeDf.yview)
        xs = ttk.Scrollbar(self, orient = 'horizontal', command = self.treeDf.xview)
        self.treeDf['yscrollcommand'] = ys.set
        self.treeDf['xscrollcommand'] = xs.set
        
        self.treeDf.grid(column=0,row=0,sticky='NSEW')
        xs.grid(column=0,row=1, sticky='WE')
        ys.grid(column=1,row=0,sticky='ns')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)


