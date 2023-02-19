#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:37:12 2023

@author: antoiovi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:36:36 2023

@author: antoiovi

-- Agginto grab a winprogresbar per bloccare frame principale :
    https://stackoverflow.com/questions/15363923/disable-the-underlying-window-when-a-popup-is-created-in-python-tkinter
"""

import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')

from numpy import arange, sin, pi


from matplotlib.backends.backend_tkagg import     FigureCanvasTkAgg, NavigationToolbar2Tk

from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import queue, threading, time
      
class WinProgressBar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Barr progress")
        self.geometry("300x200")
        self.progressbar = ttk.Progressbar(self, mode="indeterminate")
        self.progressbar.place(x=30, y=60, width=200)
        self.progressbar.start(20)

class FramePlot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        container=tk.Frame(self)
        container.grid(column=0, row=0)
        
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        ax = self.fig.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")
        '''
            CREA UN CANVAS CON DENTRO LA Figure
        '''
        canvas = FigureCanvasTkAgg(self.fig, master=container)  # A tk.DrawingArea.
        # Render the Figure.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=5)
        
        # AGGIUNGO IL TOOLBAR AL CANVAS
        toolbar = NavigationToolbar2Tk(canvas, container)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas=canvas
    
    def create_figure(self):
        
    def plot(self,x=0):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01+x)
        ax = self.fig.add_subplot()
        line, = ax.plot(t, 2 * np.sin(2 * np.pi * t)+x)
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")            
        self.canvas.draw()

        

# =============================================================================
# def MAIN():
#     PB = q.get()
#     for i in np.arange(10):
#         time.sleep(0.2)
#         print(i)
#         PB.step(10)
#         PB.update()
#     print("Done")
# 
# =============================================================================



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Progressbar example")
        self.button = tk.Button(self, text="Start", command=self.start_action)
        self.button.pack(padx=10, pady=10)
        self.frmplot=FramePlot(self)
        self.frmplot.pack()
    
    def start_action(self):
        self.button.config(state=tk.DISABLED)
        #self.button.config(state=tk.ACTIVE)

        
        t = threading.Thread(target=self.consumer)
        t.start()

        self.windows_bar = WinProgressBar(self)
        self.windows_bar.grab_set()

        self.check_thread() # run first time
        
    def consumer(self):
        self.running = True
        self.frmplot.plot()

        for i in range(100):
            print("está contando", i)
            self.frmplot.plot(i)

        self.running = False

    def check_thread(self):
        if self.running:
            self.after(1000, self.check_thread) # run again after 1s (1000ms)
        else:
            print('stop')
            self.windows_bar.grab_release()
            self.windows_bar.progressbar.stop()
            self.windows_bar.destroy()
            self.button.config(state=tk.NORMAL)
        

if __name__ == "__main__":
    f="../data/enviromental.csv"
    df=pd.read_csv(f,sep=';',decimal='.')
    print(df)
    app = App()
    app.mainloop()

# =============================================================================
# 
# PB = ttk.Progressbar(root, orient = "horizontal",length=300, mode = 'determinate')
# PB.pack()
# q = queue.Queue()
# q.put(PB)
# 
# plotsomething()
# 
# T = threading.Thread(target=MAIN(), name="MAIN")
# T.start()
# T.join()
# 
# =============================================================================
