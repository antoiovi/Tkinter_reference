#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:08:31 2022

@author: antoiovi
"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width


class Dialog(tk.Toplevel):
 def __init__(self, parent,message):
        super().__init__(parent)
        text_box = tk.Text(self)
        text_box.pack(fill=tk.BOTH)
        text_box.config(state='normal')
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, message)
        text_box.config(state='disabled')

   
class MainApplication(tk.Frame):
    def error_message(self):
        # An error box
        tk.messagebox.showerror("Error","No disk space left on device")
    def warning_message(self):
        # A warning box 
        tk.messagebox.showwarning("Warning","Could not start service")
    def info_message(self):
        # A warning box 
        # An information box
        tk.messagebox.showinfo("Information","Created in Python.")
    def extendedtext_message(self):
        msg=" This is an extended text message, cause tkMessageBox seems not able\nto include large text! "
        dialog =Dialog(self,message=msg) #Here

        
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        button1=ttk.Button(self,text="Errore message ",command=self.error_message).pack(side=tk.LEFT)
        button2=ttk.Button(self,text="Warninng message",command=self.warning_message ).pack(side=tk.LEFT)
        button3=ttk.Button(self,text="Info message ",command=self.info_message ).pack(side=tk.LEFT)
        button4=ttk.Button(self,text="Extended text message ",command=self.extendedtext_message).pack(side=tk.LEFT)
        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame message box test ")
    MainApplication(root).grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    root.mainloop()