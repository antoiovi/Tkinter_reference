#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:25:55 2022

@author: antoiovi
https://stackoverflow.com/questions/63061101/scrollbars-for-matplotlib-figure-in-tkinter



matplotlib figures are canvases. 
Therfore, its container frame won't resize to it, and bbox("all") won't work.
 Instead, we have to update the matplotlib canvas size to match the figure size
 and the toplevel canvas scrollregion to the figure size.


OKOKOK  Ok Ok Ok Ok 

"""

import os

from PIL import Image

import tkinter as tk
from tkinter import ttk, filedialog

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")
mpl.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy as np

from functools import partial

#Matplotlib Default DPI
DEFAULT_DPI = 100

#Matplotlib Default PPI
DEFAULT_PPI = 72

class AutoScrollbar(ttk.Scrollbar):

    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent

        super().__init__(self.parent,
                         *args,
                        **kwargs)

    def set(self,
            low,
            high):
        '''
            When the widget view is modified,
            the widget notifies the scrollbar by calling the set method.
            
        '''
        if float(low) <= 0.0 and float(high) >= 1.0:
            self.tk.call('grid',
                         'remove',
                         self)
        else:
            self.grid()
        ttk.Scrollbar.set(self,
                          low,
                          high)

class DoubleScrollbarFrame(ttk.Frame):

    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent

        super().__init__(self.parent,
                         *args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
                
        matplotlib figures are canvases. 
        Therfore, its container frame won't resize to it, and bbox("all") won't work.
         Instead, we have to update the matplotlib canvas size to match the figure size
         and the toplevel canvas scrollregion to the figure size.

        '''
        self.canvas = tk.Canvas(self)
        self.frame = ttk.Frame(self.canvas)
        self.scroll_x = AutoScrollbar(self,
                                      orient = tk.HORIZONTAL)
        self.scroll_y = AutoScrollbar(self,
                                      orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        
        self.canvas.config(xscrollcommand = self.scroll_x.set,
                           yscrollcommand = self.scroll_y.set)
        self.scroll_x.config(command = self.canvas.xview)
        self.scroll_y.config(command = self.canvas.yview)
        
        self.canvas.create_window((0,0),
                                  window = self.frame,
                                  anchor = 'nw')
        
        self.frame.bind('<Configure>',
                        self.set_scrollregion)

    def position_widgets(self,
                         **kwargs):
        '''
        '''
        self.scroll_x.grid(row = 1,
                           column = 0,
                           sticky = 'ew')

        self.scroll_y.grid(row = 0,
                           column = 1,
                           sticky = 'ns')

        self.canvas.grid(row = 0,
                         column = 0,
                         sticky = 'nsew')

        self.sizegrip.grid(row = 1,
                           column = 1,
                           sticky = 'se')

        #NOTE: Do not use geometry manager with `self.frame`. This will
        # pass control from the canvas to grid and the canvas will then
        # no longer know how much to grow.
        
    def set_scrollregion(self,
                         event):
        '''
        '''
        self.canvas.configure(scrollregion = self.canvas.bbox('all'))

class Graph(ttk.Frame):

    def __init__(self,
                 parent,
                 axis_off = True,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent
        self.axis_off = axis_off

        super().__init__(self.parent,
                         *args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
   
            
        fg=sns.relplot(  data=fmri, x="timepoint", y="signal" , col="region",  hue="event", style="event", kind="line",)
      
        self.figure =fg.figure
        size = self.figure.get_size_inches()*self.figure.dpi # size in pixels
        print("SIZE>>>",size)
        self.axis = self.figure.axes[0]

        #if self.axis_off:
        #    self.axis.set_axis_off()

        self.canvas = tk.Canvas(self)
        self.frame = ttk.Frame(self.canvas)

        self.mpl_canvas = FigureCanvasTkAgg(self.figure,
                                            self.frame)

        self.mpl_canvas.draw()

        self.scroll_x = AutoScrollbar(self,
                                      orient = tk.HORIZONTAL)
        self.scroll_y = AutoScrollbar(self,
                                      orient = tk.VERTICAL)
        self.sizegrip = ttk.Sizegrip(self)
        
        self.canvas.config(xscrollcommand = self.scroll_x.set,
                           yscrollcommand = self.scroll_y.set)
        self.scroll_x.config(command = self.canvas.xview)
        self.scroll_y.config(command = self.canvas.yview)
        
        self.cwid = self.canvas.create_window((0,0),
                                              window = self.frame,
                                              anchor = 'nw')

        self.frame.bind('<Configure>',
                        self.set_scrollregion)

        self.toolbar_frame = ttk.Frame(self)

        self.toolbar = NavigationToolbar2Tk(self.mpl_canvas,
                                            self.toolbar_frame)

    def set_scrollregion(self,
                         event):
        '''
        '''
        w, h = self.figure.get_size_inches()
        #print("Scroll region",w,h)
        w = int(w * DEFAULT_DPI)
        h = int(h * DEFAULT_DPI)
        scrollregion = (0,0,w,h)
        
        self.canvas.configure(scrollregion = scrollregion)
        
    def position_widgets(self):
        '''
        '''
        self.scroll_x.grid(row = 1,
                           column = 0,
                           sticky = 'ew')

        self.scroll_y.grid(row = 0,
                           column = 1,
                           sticky = 'ns')

        self.canvas.grid(row = 0,
                         column = 0,
                         sticky = 'nsew')

        self.mpl_canvas.get_tk_widget().grid(row = 0,
                                             column = 0,
                                             sticky = 'nsew')

        self.sizegrip.grid(row = 1,
                           column = 1,
                           sticky = 'se')

        #NOTE: Do not use geometry manager with `self.frame`. This will
        # pass control from the canvas to grid and the canvas will then
        # no longer know how much to grow.

        self.toolbar.update()
        self.toolbar_frame.grid(row = 2,
                                column = 0,
                                sticky = 'sew')

    def load_image(self,
                   path):
        '''
        '''
        
        self.mpl_canvas.flush_events()
        self.axis.clear()
        self.frame.destroy()
        print("CREO WIDGET")
        self.create_widgets()
        print("POSIZIONO WIDGETS")
        self.position_widgets()
        self.mpl_canvas.draw()
        self.canvas.update()
        return
        # Disegno figure in axes
        #fg=sns.lineplot(  data=fmri, x="timepoint", y="signal", ax=self.axis,    hue="event", style="event")
        
        print("CREO FACET GRID")
        fg=sns.relplot(  data=fmri, x="timepoint", y="signal" , col="region",  hue="event", style="event",kind='line')
        self.figure=fg.figure
        self.axis = self.figure.axes[0]
        if self.axis_off:
            self.axis.set_axis_off()
        self.figure.set_canvas(self.mpl_canvas)
        
        size = self.figure.get_size_inches()*self.figure.dpi # size in pixels
        print("-->SIZE",size)
        self.graph_w_in =size[0]
        self.graph_h_in =size[1]
        
        
        self.mpl_canvas.get_tk_widget().configure(
            width = self.graph_w_in ,
            height = self.graph_h_in )
        
        self.mpl_canvas.draw()
        self.canvas.update()
        return
        self.image = Image.open(path)

        #NOTE: Dots per inch (dpi) in matplotlib should be used for
        # printing to paper media only. dpi is set at the time of
        # printing/scanning. Computer screen resolution is fixed by
        # the screen hardware and given in pixels per inch (ppi).
        # An image scanned at higher dpi will appear crisper on a
        # computer screen because of the difference in halftone/
        # dithering at each pixel, but the total size and number of
        # pixels in the image will be the same.
        # Matplotlib use 72 pixels per inch (ppi) for its figures by
        # default, and this cannot be changed. Thus, if you increase
        # dots per inch (dpi), the figure will appear bigger when
        # printed to screen (i.e. on the computer monitor) because
        # it will use more pixels to represent the same features.
        # When printed to paper media, however, the image will be
        # the same size regardless of dpi, but have finer halftoning/
        # dithering for an improved appearance.
        # Matplotlib sets sizes in terms of inches, so the scan dpi
        # must be known in order to get the physical size of the
        # image.
        if self.image.info.get('dpi'):
            self.scan_dpi, _ = self.image.info['dpi']
        else:
            self.scan_dpi = DEFAULT_DPI # matplotlib default
            
        self.w_pel, self.h_pel = self.image.size

        self.graph_w_in = self.w_pel / self.scan_dpi
        self.graph_h_in = self.h_pel / self.scan_dpi        
        
        self.figure.set_size_inches(self.graph_w_in,
                                    self.graph_h_in)
        
        self.image = np.array(self.image)
        
        self.axis.imshow(self.image)

        self.mpl_canvas.get_tk_widget().configure(
            width = self.graph_w_in * DEFAULT_DPI,
            height = self.graph_h_in * DEFAULT_DPI)
        
        self.mpl_canvas.draw()
        self.canvas.update()

class FileBrowser(tk.Frame):

    def __init__(self,
                 parent,
                 path_type = 'file',
                 label_text = '',
                 file_types = (('*','All File Types...'),),
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent
        self.path_type = path_type
        self.label_text = label_text
        self.file_types = file_types
        
        super().__init__(parent,
                         *args,
                         **kwargs)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.label = tk.Label(self.parent,
                              text = self.label_text)

        self.path_entry = tk.Entry(self.parent,
                                   width = 50)

        self.button = ttk.Button(self.parent,
                                 text = 'Browse...',
                                 command = partial(self.open_file_dialog,
                                                   self.path_type,
                                                   self.file_types))

    def position_widgets(self):
        '''
        '''
        opts = {'padx': (5,5),
                'pady': (5,5)}
        
        self.label.grid(row = 0,
                        column = 0,
                        sticky = 'e',
                        **opts)
        self.path_entry.grid(row = 0,
                             column = 1,
                             sticky = 'w',
                             **opts)
        self.button.grid(row = 0,
                         column = 2,
                         sticky = 'w',
                         **opts)

    def open_file_dialog(self,
                         path_type,
                         file_types):
        '''
        '''
        init_dir = os.getcwd()

        if path_type == 'file':
             self.path = filedialog.askopenfilename(initialdir = init_dir,
                                                    title = 'Select file...',
                                                    filetypes = file_types)
        elif path_type == 'directory':
            self.path = filedialog.askdirectory(initialdir = init_dir,
                                                title = 'Select directory...')

        self.path_entry.delete(0,tk.END)
        self.path_entry.insert(0,self.path)

    def get_path(self):
        '''
        '''
        return self.path_entry.get()

class Loader(ttk.Frame):
    '''
    '''
    def __init__(self,
                 parent,
                 *args,
                 **kwargs):
        '''
        '''
        self.parent = parent

        super().__init__(self.parent,
                         *args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.input_label_frame = ttk.LabelFrame(self,
                                                text = 'Input')
        self.output_label_frame = ttk.LabelFrame(self,
                                                 text = 'Output')
        
        self.create_file_browser(self.input_label_frame)
        self.create_ok_button(self.input_label_frame)

        self.create_output_window(self.output_label_frame)

    def create_file_browser(self,
                            label_frame):
        '''
        '''
        self.browser_frame = ttk.LabelFrame(label_frame,
                                            text = 'Select File')
        self.file_browser = FileBrowser(self.browser_frame,
                                        path_type = 'file',
                                        label_text = 'File:',
                                        file_types = (('*.tif', 'TIF'),
                                                      ('*.png', 'PNG'),))

    def create_ok_button(self,
                         label_frame):
        '''
        '''
        self.input_ok_button = ttk.Button(label_frame,
                                          text = 'OK',
                                          command = self.calibrate)

    def calibrate(self):
        '''
        '''
        self.graph.load_image("")

        path = self.file_browser.get_path()

        if path == '':
            tk.messagebox.showerror(title = 'No File Selected',
                                 message = 'No file chosen. Please select file.')
            return

        _, ext = os.path.splitext(path)

        if ext.lower() not in ('.tif', '.png'):
            tk.messagebox.showerror(title = 'File Is Not \"*.tif\" or \"*.png\"',
                                 message = 'File must be a \"*.tif\" or \"*.png\" image file. Please reselect file and try again.')

        img = plt.imread(path)

        self.graph.load_image(path)
        
    def create_output_window(self,
                             label_frame):
        '''
        '''
        self.output_frame = ttk.Frame(label_frame)
        self.graph = Graph(self.output_frame)

    def position_widgets(self,
                         **kwargs):
        '''
        '''
        #OK Button
        self.input_ok_button.grid(row = 4,
                                  column = 0,
                                  sticky = 'e')
        
        #Frames
        self.input_label_frame.grid(row = 0,
                                    column = 0,
                                    sticky = 'nsew')
        
        self.browser_frame.grid(row = 1,
                                column = 0,
                                sticky = 'nw')

        self.file_browser.grid(row = 0,
                               column = 0,
                               sticky = 'nsew')

        self.output_label_frame.grid(row = 0,
                                     column = 1,
                                     sticky = 'nw')

        self.graph.grid(row = 0,
                        column = 0,
                        sticky = 'nsew')

        self.output_frame.grid(row = 0,
                               column = 0,
                               sticky = 'nsew')


class MainApp(tk.Tk):

    def __init__(self,
                 title,
                 *args,
                 **kwargs):
        '''
        '''
        self._title = title

        super().__init__(*args,
                         **kwargs)

        #Set widgets to fill main window such that they are
        #all the same size
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #Set window title
        self.title(self._title)

        self.create_widgets()
        self.position_widgets()

    def create_widgets(self):
        '''
        '''
        self.loader = Loader(self)

    def position_widgets(self):
        '''
        '''
        self.loader.grid(row = 0,
                         column = 0,
                         sticky = 'nsew')

if __name__ == '__main__':

    #Create GUI
    root = MainApp('MainApp')

    #Run program
    root.mainloop()