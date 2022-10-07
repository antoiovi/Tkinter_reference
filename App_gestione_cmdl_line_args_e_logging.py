#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:29 2022

@author: antoiovi

App to test the handle of command line arguments in a tkinter application 
an the setting of a logger

"""


import tkinter as tk
from tkinter import BOTH, ttk

import sys,getopt # Per gestire parametri da command line
import logging


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
    x=0
    def button1_click(self):
        s=str(self.x)
        self.label1.config(text=s)
        self.x=self.x+1
    
    def set_message(self,msg):
        self.text_box.delete('1.0',tk.END)
        self.text_box.insert('end', msg)

        return
    
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        #self.title("Frame UNO")
        #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
        #self.geometry('1000x800')
        button1=ttk.Button(self,text="Bottone 1",command=self.button1_click)
        button1.grid(column=0,row=0,sticky='w')
        self.label1=ttk.Label(self,text="Etichetta 1")
        self.label1.grid(column=1,row=0,sticky='w')
        self.text_box = tk.Text(self, wrap="none",width=50)
        self.text_box.grid(column=0,row=1,  sticky='wens')
        
        
        statusbar=Statusbar(self)
        statusbar.grid(column=0,row=2,sticky='NWES',padx=5,pady=5)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=1)


if __name__ == "__main__":
    LOG_LEVEL=logging.ERROR
    argv=sys.argv[1:]
    '''
    getopt.getopt(args, options, [long_options])
    
    '''
    validargs= "Argomenti ed opzioni valide :\n\t -l [DEBUG ,INFO,WARNING,ERROR,CRITICAL]\n\toppure"+\
      "\t-l [D ,I,W,E,C]\n\toppure"+\
      "\t--loglevel=[DEBUG ,INFO,WARNING,ERROR,CRITICAL]\n\toppure"+\
      "\t--loglevel= [D ,I,W,E,C]"

    print(argv)
    
    messaggio="Riga di comando : "
    for x in argv:
        messaggio=messaggio+" "+str(x)
    messaggio=messaggio+"\n"
    try:
      opts, args = getopt.getopt(argv,'-l,-D,-I,-W,-E,-C',["loglevel="])
      for opt, arg in opts:
          messaggio=messaggio+"Option " +opt+"  Arg : " +arg+"\n"
          if opt in ('-l','--loglevel'):
              print("Opts is : ",opt,"   ARG ",arg)
              if arg  in ['DEBUG','D']:
                  LOG_LEVEL=logging.DEBUG
              elif arg in ['INFO','I']:
                  LOG_LEVEL=logging.INFO
              elif arg in ['WARNING','W']:
                  LOG_LEVEL=logging.WARNING
              elif arg in ['ERROR','E']:
                  LOG_LEVEL=logging.ERROR
              elif arg in ['CRITICAL','C']:
                  LOG_LEVEL=logging.CRITICAL
          elif opt in('-D','-I','-W','-E','-C'):
              print("Opts is : ",opt)
              if opt=='-D':
                  LOG_LEVEL=logging.DEBUG
              elif opt=='-I':
                  LOG_LEVEL=logging.INFO
              elif opt=='-W':
                  LOG_LEVEL=logging.WARNING
              elif opt=='-E':
                  LOG_LEVEL=logging.ERROR
              elif opt=='-C':
                  LOG_LEVEL=logging.CRITICAL
          else:
              messaggio=messaggio+"\n\t"+opt +" is not valid argument.\n"+validargs
              print(messaggio)
    except getopt.GetoptError:
              messaggio=messaggio+"\n\t not valid argument.\n GetoptError:\n"+validargs
              print(messaggio)
 
 
    logging .basicConfig(format='[%(levelname)s][%(module)s][%(funcName)s] %(message)s '
                    , level=LOG_LEVEL)

    logger= logging.getLogger(__name__)
    
    logger.debug("We are in debug ...")
    logger.info("We are in info ...")
    logger.warning("We are in warning ...")
    logger.error("We are in error ...")
    logger.critical("We are in critical ...")
    #sys.exit(0)
    
    root = tk.Tk()
    root.title("Test command line arguments and logger ")
    content=tk.Frame(root,bg='green')
    #tk.Tk ha la proprieta geometry,; tk.Frame non c'e l'ha
    root.geometry('500x400')
    # styck (NSEW) espande il content in tutta la root 
    content.grid(column=0,row=0,sticky='NWES') 
    # styck (NSEW) espande mainapplication nel content
    mainapp=MainApplication(content)
    messaggio=messaggio+"\n\n\n"+validargs
    mainapp.set_message(messaggio)
    mainapp.grid(column=0,row=0,sticky='WENS')#.pack(side="top", fill="both", expand=True)
    # Senza questa riga content non occupa tutto il frame root    
    content.columnconfigure(0,weight=1)
    content.rowconfigure(0,weight=1)
    # Senza questa riga root non occupa tutto il frame della applicazione    
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    #root.pack(   fill='x')
    root.mainloop()