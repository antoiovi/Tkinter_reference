#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    After Callbacks

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

    
    After Callbacks

The after method is documented in
 after(3tcl)(https://www.tcl.tk/man/tcl/TclCmd/after.html)
, and it’s an easy way to run stuff in Tk’s main loop. 
All widgets have this method, and it doesn’t matter 
which widget’s after method you use. any_widget.after(milliseconds, callback) 
runs callback() after waiting for the given number of milliseconds. 
The callback runs in Tk’s mainloop, so it must not take a long time to run.

For example, this program displays a simple clock with after callbacks and 
time.asctime:

"""
import time
import tkinter
from tkinter import ttk


# this must return soon after starting this
def change_text():
    label['text'] = time.asctime()

    # now we need to run this again after one second, there's no better
    # way to do this than timeout here
    root.after(1000, change_text)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame, text='0')
label.pack()

change_text()      # don't forget to actually start it :)

root.geometry('200x200')
root.mainloop()

'''
It’s also possible to pass arguments to after callbacks:

# run print('hello') after 1 second
any_widget.after(1000, print, 'hello')

# run foo(bar, biz, baz) after 3 seconds
any_widget.after(3000, foo, bar, biz, baz)
'''