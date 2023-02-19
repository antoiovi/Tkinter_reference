#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi

Tkinter application to test the widgets disabling
while thread and progress bar is runninag

"""


import tkinter as tk
from tkinter import BOTH, ttk
from turtle import width

import threading
class WinProgressBar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Barr progress")
        self.geometry("300x200")
        self.progressbar = ttk.Progressbar(self, mode="indeterminate")
        self.progressbar.place(x=30, y=60, width=200)
        self.progressbar.start(20)

class FrameTextField(tk.Frame):
    def deleteInput(self):
        self.textField.delete(0,tk.END)
        return

    def resetText(self):
        self.textField.delete(0,tk.END)
        self.textField.insert(0,"#####")
        return
    
    def disableText(self):
        self.textField.config(state='disabled')
        return

    def enableText(self):
        self.textField.config(state='normal')
        return
    def printText(self):
        print(self.value.get())
        return

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        ttk.Label(self, text="Campo di testo ttk.Entry :").pack(side=tk.LEFT)
        self.value= tk.StringVar(self,'A')    
        self.textField=ttk.Entry(self,textvariable=self.value  ,width=30)
        self.textField.pack(side=tk.LEFT)
        ttk.Button(self,text="Delete",command=self.deleteInput).pack(side=tk.LEFT)
        ttk.Button(self,text="Reset",command=self.resetText).pack(side=tk.LEFT)
        ttk.Button(self,text="Disable",command=self.disableText).pack(side=tk.LEFT)
        ttk.Button(self,text="Enable",command=self.enableText).pack(side=tk.LEFT)
        ttk.Button(self,text="Print",command=self.printText).pack(side=tk.BOTTOM)
        

class FrameTextBox(tk.Frame):
    '''
    index(index) – To get the specified index. 
    insert(index) – To insert a string at a specified index. 
    see(index) – Checks if a string is visible or not at a given index. 
    get(startindex, endindex) – to get characters within a given range. 
    delete(startindex, endindex) – deletes characters within specified range.
    
    
    Index :
        The "1.0" indicates exactly that: you want to get the content starting from line 1 and character 0 
    '''
    
    
    def deleteInput(self):
        self.text_box.delete('1.0',tk.END)
        return
    def resetText(self):
        self.text_box.delete('1.0',tk.END)
        self.text_box.insert('end', "Lorem ipsum...\n...\n...")
        return
    def disableText(self):
        self.text_box.config(state='disabled')
        return
    def enableText(self):
        self.text_box.config(state='normal')
        return
    def printText(self):
        # riga 1 carattere 0 --> 1.0
        print(self.text_box.get('1.0',tk.END))
        print("tk.END = ",tk.END)
        return
    def append(self):
        message='X'
        self.text_box.insert('end',message)

    def set_message(self,message):
        self.text_box.delete('1.0',tk.END)
        self.text_box.insert('end', message)

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #self.text_box = tk.Text(self)
        # Metto wrap="none"  per permettere lo scrolling orzzontale
        self.text_box = tk.Text(self, wrap="none",width=50)
        ys = ttk.Scrollbar(self, orient = 'vertical', command = self.text_box.yview)
        xs = ttk.Scrollbar(self, orient = 'horizontal', command = self.text_box.xview)
        self.text_box['yscrollcommand'] = ys.set
        self.text_box['xscrollcommand'] = xs.set
        self.text_box.insert('end', "Lorem ipsum...\n...\n...")
        self.text_box.insert('end', "Lorem ipJDLKAJSDKJFLKASJDFLASJFÀJASÀFJÀAJDÀJASDÀFJAÀSJFÀAJSDÀFJASÀDJFÀAJSD  AJSÒLJFÀALSJ JASDÀJF  JALKSJDFKJASÀsum...\n...\n...")
        self.text_box.grid(column = 0, row = 0, sticky = 'nwes')
        xs.grid(column = 0, row = 1, sticky = 'we')
        ys.grid(column = 1, row = 0, sticky = 'ns')
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)     
        rigacomandi=tk.Frame(self)
        self.btnDelete=ttk.Button(rigacomandi,text="Delete",command=self.deleteInput)
        self.btnDelete.pack(side=tk.LEFT)
        ttk.Button(rigacomandi,text="Reset",command=self.resetText).pack(side=tk.LEFT)
        ttk.Button(rigacomandi,text="Append x",command=self.append).pack(side=tk.LEFT)
        ttk.Button(rigacomandi,text="Disable",command=self.disableText).pack(side=tk.LEFT)
        ttk.Button(rigacomandi,text="Enable",command=self.enableText).pack(side=tk.LEFT)
        ttk.Button(rigacomandi,text="Print",command=self.printText).pack(side=tk.LEFT)
        rigacomandi.grid(column=0,row=2,    columnspan=2)

        
class Statusbar(tk.Frame):
     def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.messagelbl=ttk.Label(self, text="Status bar")
        self.btnStartThread=ttk.Button(self,
                                       text="Start resource consuming thread")
        #  START THREAD BUTTON
        self.btnStartThread.grid(column=0, row=0)
        self.messagelbl.grid(column=1, row=0)

     def update(self,program_event):
        return
        

    
class MainApplication(tk.Frame):
        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frameTextField=FrameTextField(self)
        self.frameTextField.grid(column=0,row=0,sticky='w')
        self.frameTxtBox=FrameTextBox(self)
        self.frameTxtBox.grid(column=0,row=1)
        
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='NWES',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=0)
        
        # START BUTTON BIND
        statusbar.btnStartThread.bind('<Button-1>',self.start_my_thread)
    
    
    def start_my_thread(self,event):
        '''
         START THREAD
        '''
        #self.button.config(state=tk.DISABLED)
        
        t = threading.Thread(target=self.resource_consumer)
        t.start()
        
        self.windows_bar = WinProgressBar(self)

        self.check_thread() # run first time
        
        
    def resource_consumer(self):
        self.running = True
        for i in range(500):
            print("Counting number :", i)
        self.running = False

    def check_thread(self):
        if self.running:
            self.off_all()
            self.after(1000, self.check_thread) # run again after 1s (1000ms)
        else:
            print('stop')
            self.windows_bar.progressbar.stop()
            self.windows_bar.destroy()
            self.on_all()
            #self.button.config(state=tk.NORMAL)
    
   

    
    def on_all(self):
        for child in self.frameTextField.winfo_children():
            print(child.widgetName) 
        for child in self.frameTxtBox.winfo_children():
            print(child.widgetName) 
        for child in self.frameTxtBox.winfo_children():
            print(child.widgetName)    

            try:
                if child.widgetName == 'text':  # frame has no state, so skip
                   child.configure(state='normal')
            except Exception as e:
                print(e)
    
    def off_all(self):
        for child in self.frameTxtBox.winfo_children():
            try:
                if child.widgetName == 'text':  # frame has no state, so skip
                    print(child.widgetName)    
                    child.configure(state='disabled')
            except Exception as e:
                print(e) 




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame UNO")
    content=tk.Frame(root,bg='green')
    #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
    root.geometry('800x400')
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