#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:01:39 2023

@author: 
    https://codeahoy.com/learn/tkinter/ch2/#blocking-callback-functions
    
Using Event Loop and Threads in Tkinter
        https://codeahoy.com/learn/tkinter/ch5/
        
 When a tkinter program is running, Tk needs to process different kinds of events. 
 For example, clicking on a button generates an event, and the main loop must 
 make the button look like it’s pressed down and run our callback. 
 Tk and most other GUI toolkits do that by simply checking for any new events
 over and over again, many times every second. This is called an event loop or 
 main loop.

Button callbacks are also ran in the main loop. So if our button callback 
takes 5 seconds to run, the main loop can’t process other events while 
it’s running. For example, it can’t close the root window when we try to 
close it. That’s why everything froze with our time.sleep(5) callback.

    https://codeahoy.com/learn/tkinter/ch2/#blocking-callback-functions

"""
import time
import tkinter
from tkinter import ttk


def ok_callback():
    print("hello")


def stupid_callback():
    time.sleep(5)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button1 = ttk.Button(big_frame, text="This is OK", command=ok_callback)
button1.pack()
button2 = ttk.Button(big_frame, text="This sucks", command=stupid_callback)
button2.pack()

root.mainloop()