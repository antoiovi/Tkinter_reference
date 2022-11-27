#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:26:38 2022

@author: https://stackoverflow.com/questions/45847313/what-does-weight-do-in-tkinter
"""

import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

f1 = tk.Frame(root, background="bisque", width=10, height=100)
f2 = tk.Frame(root, background="pink", width=10, height=100)

f1.grid(row=0, column=0, sticky="nsew")
f2.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=2)

root.mainloop()