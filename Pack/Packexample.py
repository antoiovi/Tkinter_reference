#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:00:28 2022

@author: https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method



    The fill option tells the manager that the widget wants fill the entire 
    space assigned to it. The value controls how to fill the space; BOTH means 
    that the widget should expand both horizontally and vertically, X means that 
    it should expand only horizontally, and Y means that it should expand only vertically.

    The expand option tells the manager to assign additional space to the widget box. 
    If the parent widget is made larger than necessary to hold all packed widgets, 
    any exceeding space will be distributed among all widgets that have the expand 
    option set to a non-zero value.




"""

import tkinter as tk

root = tk.Tk()
root.geometry()

for e, expand in enumerate([False, True]):
    for f, fill in enumerate([None, tk.X, tk.Y, tk.BOTH]):
        for s, side in enumerate([tk.TOP, tk.LEFT, tk.BOTTOM, tk.RIGHT]):
            position = '+{}+{}'.format(s * 205 + 100 + e * 820, f * 235 + 100)
            win = tk.Toplevel(root)
            win.geometry('200x200'+position)
            text = str("side='{}'\nfill='{}'\nexpand={}".format(side, fill, str(expand)))
            tk.Label(win, text=text, bg=['#FF5555', '#55FF55'][e]).pack(side=side, fill=fill, expand=expand)
                
root.mainloop()