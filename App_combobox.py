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
    def selectedState(self):
        state=self.strvarSelected.get()
        self.text_box.config(state='normal')
        self.text_box.insert(tk.END, state)
        self.text_box.config(state='disabled')     
    def OptionCallBack(self,*args):
        tk.messagebox.showinfo( "Selected state", self.strvarSelected.get())

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        '''
        Due opzioni : 
                1 - con un pulsante richiamo una funzione (selectedState) dove
                        recupero il valore selezionato
                    OPPURE
                2 - automaticamente quando cambia la selezione chiama
                    la funzione OptionCallBack
        '''
        
         # Combobox creation
        self.strvarSelected = tk.StringVar()
        # per attivare la funzione quando si seleziona un elemento del combo box
        self.strvarSelected.trace_add('write', self.OptionCallBack)
        
        cboxStates = ttk.Combobox(self, width = 27, 
                                  textvariable = self.strvarSelected)
        
        
        btn1=tk.Button(self,text='Select state',command=self.selectedState)
        btn1.grid(column = 1, row = 0)
          
        # Adding combobox drop down list
        cboxStates['values'] = (' USA', ' France', ' Italy',' Greek', ' Spain', )
          
        cboxStates.grid(column = 0, row = 0)
        cboxStates.current(0)
        self.text_box = tk.Text(self)
        self.text_box.grid(column=0,row=1,columnspan=2)
  

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Combo box ")
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