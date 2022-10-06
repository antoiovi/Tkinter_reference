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



class FrameRadioB(tk.Frame):
                
        def value_picked(self):
            picked=self.selected_value.get()
            print("Valore selezionato ",picked)
            self.parent.radio_button_changed(picked)
            return
        
        def __init__(self, parent,*args, **kwargs):
            tk.Frame.__init__(self, parent, *args, **kwargs)
            self.parent=parent
            self.selected_value= tk.StringVar(self,'A')    
            values= (('Value A', 'A'),
                     ('Value B', 'B'),
                     ('Value C', 'C'),
                     )
        
            label = ttk.Label(self,text="Valori da selezionare")
            label.pack(fill='x', padx=5, pady=5 ,side='left')
        
            for val in values:
                radio = ttk.Radiobutton(
                    self,
                    text=val[0],
                    value=val[1],
                    variable=self.selected_value,
                    command=self.value_picked
                )
                radio.pack(fill='x', padx=5, pady=5,    side='left')

class FrameCheckB(tk.Frame):
    def value_picked(self):

        if (self.var1.get() == 1) & (self.var2.get() == 0):
            self.parent.chebox_clicked('I love Python ')
        elif (self.var1.get() == 0) & (self.var2.get() == 1):
            self.parent.chebox_clicked('I love C++')
        elif (self.var1.get() == 0) & (self.var2.get() == 0):
            self.parent.chebox_clicked('I do not anything')
        else:
            self.parent.chebox_clicked('I love both')
        return
    
    def __init__(self, parent,*args, **kwargs):    
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent=parent
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        
        c1 = ttk.Checkbutton(self, text='Python',variable=self.var1, onvalue=1, offvalue=0, command=self.value_picked)
        c1.pack(side='left')
        c2 = ttk.Checkbutton(self, text='C++',variable=self.var2, onvalue=1, offvalue=0, command=self.value_picked)
        c2.pack(side='left')


class MainApplication(tk.Frame):
    
    def radio_button_changed(self,value):
        print(value)
        message="Radio button selezionato : "+str(value)
        self.text_box.config(state='normal')
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, message)
        self.text_box.config(state='disabled')
    
    def chebox_clicked(self,value):
        print(value)
        message="Stato dei check box: "+str(value)
        self.text_box.config(state='normal')
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, message)
        self.text_box.config(state='disabled')
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        radioframe=FrameRadioB(self)
        radioframe.grid(column=0,row=0)
        
        checkboxframe=FrameCheckB(self)
        checkboxframe.grid(column=0,row=1)
        
        self.text_box = tk.Text(self)
        self.text_box.grid(column=0,row=2)
        
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=3,sticky='WE',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=0)


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