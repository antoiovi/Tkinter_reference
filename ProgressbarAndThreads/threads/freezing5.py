#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://codeahoy.com/learn/tkinter/ch5/

https://docs.python.org/3/library/queue.html

Moving stuff from threads to tkinter

The thread world and tkinter’s mainloop world must be separated from each other, 
but we can move stuff between them with queues. 

Usually I need queues for getting stuff from threads back to tkinter. 
The thread puts something on the queue, and then an after callback gets 
it from the queue with block=False. Like this:


"""
import queue
import threading
import time
import tkinter
from tkinter import ttk

the_queue = queue.Queue()


def thread_target():
    for number in range(10):
        print("thread_target puts hello", number, "to the queue")
        the_queue.put("hello {}".format(number))
        time.sleep(1)

    # let's tell after_callback that this completed
    print('thread_target puts None to the queue')
    the_queue.put(None)


def after_callback():
    try:
        message = the_queue.get(block=False)
    except queue.Empty:
        # let's try again later
        root.after(100, after_callback)
        return

    print('after_callback got', message)
    if message is not None:
        # we're not done yet, let's do something with the message and
        # come back later
        label['text'] = message
        root.after(100, after_callback)


root = tkinter.Tk()
big_frame = ttk.Frame(root)
big_frame.pack(fill='both', expand=True)

label = ttk.Label(big_frame)
label.pack()

threading.Thread(target=thread_target).start()
root.after(100, after_callback)

root.geometry('200x200')
root.mainloop()
