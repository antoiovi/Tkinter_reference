#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:09:32 2022

@author: https://stackoverflow.com/questions/62621138/python-tkinter-how-to-use-grid-sticky
"""

import tkinter as tk
root = tk.Tk()

text1 = tk.Text(state=tk.DISABLED)
scroll = tk.Scrollbar(root, command=text1.yview)
text1.configure(yscrollcommand=scroll.set)

text1.grid(row=1, column=0,sticky='we')
scroll.grid(row=1, column=1, sticky="ns")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

root.mainloop()