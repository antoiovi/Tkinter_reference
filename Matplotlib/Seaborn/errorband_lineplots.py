'''
https://seaborn.pydata.org/examples/errorband_lineplots.html

'''

import tkinter
from typing import Callable

import numpy as np
import seaborn as sns
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
sns.set_theme(style="darkgrid")
def init_gui(root, update_function: Callable) -> FigureCanvasTkAgg:
    def event_key_press(event):
        print("you pressed {}".format(event.key))
        update_function()
        key_press_handler(event, canvas)


    # create empty figure and draw
    init_figure = create_figure()
    canvas = FigureCanvasTkAgg(init_figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    # call key press event
    canvas.mpl_connect("key_press_event", event_key_press)
    return canvas


def create_figure() -> Figure:
    # generate some data
    matrix = np.random.randint(20, size=(10, 10))
    # plot the data
    figure = Figure(figsize=(6, 6))
    ax = figure.subplots()
    # Plot the responses for different events and regions
    sns.lineplot(x="timepoint", y="signal",
                 hue="region", style="event",
                 data=fmri,ax=ax)
    return figure


def redraw_figure():
    figure = create_figure()
    canvas.figure = figure
    canvas.draw()


root = tkinter.Tk()
canvas = init_gui(root, update_function=redraw_figure)

tkinter.mainloop()
