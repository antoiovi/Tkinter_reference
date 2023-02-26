#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://codeahoy.com/learn/tkinter/ch5/

   Basic Thread Stuff

So far we have avoided using functions that take a long time to complete 
in tkinter programs, but now we’ll do that with the threading module (
    https://docs.python.org/3/library/threading.html ). 

Here’s a minimal example:
    
    That’s pretty cool. The function runs for about a second, 
    but it doesn’t freeze our GUI.

As usual, great power comes with great responsibility.
 Tkinter isn’t thread-safe, so we must not do any tkinter stuff in threads. 
 Don’t do anything like label['text'] = 'hi' or even print(label['text']). 
 It may kind of work for you, but it will make different kinds of weird
 problems on some operating systems.

Think about it like this: in tkinter callbacks we can do stuff with tkinter 
and we need to return as soon as possible, but in threads we can do stuff 
that takes a long time to run but we must not touch tkinter. 
So we can use tkinter or run stuff that takes a long time, but not both in 
the same place.
"""

import threading
import time
import tkinter
from tkinter import ttk


# in a real program it's best to use after callbacks instead of
# sleeping in a thread, this is just an example
def blocking_function():
    print("blocking function starts")
    time.sleep(1)
    print("blocking function ends")


def start_new_thread():
    thread = threading.Thread(target=blocking_function)
    thread.start()


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

button = ttk.Button(big_frame, text="Start the blocking function",
                    command=start_new_thread)
button.pack()
root.mainloop()
'''
It’s also possible to pass arguments to after callbacks:

# run print('hello') after 1 second
any_widget.after(1000, print, 'hello')

# run foo(bar, biz, baz) after 3 seconds
any_widget.after(3000, foo, bar, biz, baz)

Threads can handle arguments too, but they do it slightly differently:

# run foo(bar, biz, baz) in a thread
thread = threading.Thread(target=foo, args=[bar, biz, baz])
thread.start()
'''