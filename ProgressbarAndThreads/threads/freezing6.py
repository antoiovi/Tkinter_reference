#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://codeahoy.com/learn/tkinter/ch5/

https://docs.python.org/3/library/queue.html

Moving stuff from tkinter to threads

We can also use queues to get things from tkinter to threads.
 Here we put stuff to a queue in tkinter and wait for it in the thread,
 so we don’t need block=False. Here’s an example:


"""
import queue
import threading
import time
import tkinter
from tkinter import ttk

the_queue = queue.Queue()


def thread_target():
    '''
    The problem is that Python is waiting for our thread to return, 
    but it’s running a while True. To fix that, we need to modify our
    thread_target to stop when we put None on the queue, and then put a 
    None to the queue when root.mainloop has completed. Like this:
    '''
    while True:
        message = the_queue.get()
        if message is None:
            print("thread_target: got None, exiting...")
            return

        print("thread_target: doing something with", message, "...")
        time.sleep(1)
        print("thread_target: ready for another message")


def on_click():
    the_queue.put("hello")


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

ttk.Button(big_frame, text="Click me", command=on_click).pack()
threading.Thread(target=thread_target).start()
root.mainloop()

# we get here when the user has closed the window, let's stop the thread
the_queue.put(None)