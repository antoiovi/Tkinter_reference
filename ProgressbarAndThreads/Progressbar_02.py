#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:14:04 2023

@author: antoiovi


https://stackoverflow.com/questions/56951383/tkinter-disable-buttons-while-thread-is-running

In many GUIs you can't change GUI in thread - you have to do it in main process.

You can use queue to send information to main process which will update GUI.

In Tkinter you can use

root.after(time_in_milliseconds, function_name) 

to run periodically function which can check message from this queue.

Or it can periodically check

thread2.is_alive()



"""

import tkinter as tk
from threading import Thread
import time

def long_running_function():
    print('start sleep')
    time.sleep(3)
    print('end sleep')

def start_thread():
    global t
    global counter

    b['state'] = 'disable'
    counter = 0

    t = Thread(target=long_running_function)
    t.start()

    check_thread()
    # or check after 100ms
    # root.after(100, check_thread) 

def check_thread():
    global counter

    if not t.is_alive():
        b['state'] = 'normal'
        l['text'] = ''
    else:
        l['text'] = str(counter)
        counter += 0.1

        # check again after 100ms
        root.after(100, check_thread) 

#-----------------------------------------------------

# counter displayed when thread is running        
counter = 0

root = tk.Tk()

l = tk.Label(root)
l.pack()

b = tk.Button(root, text="Start", command=start_thread)
b.pack()

root.mainloop()