'''
https://stackoverflow.com/questions/63836979/bar-progress-in-tkinter-with-thread
'''


import threading
import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Progressbar example")
        self.button = tk.Button(self, text="Start", command=self.start_action)
        self.button.pack(padx=10, pady=10)

    def start_action(self):
        self.button.config(state=tk.DISABLED)
        
        t = threading.Thread(target=self.contar)
        t.start()

        self.windows_bar = WinProgressBar(self)

        self.check_thread() # run first time
        
    def contar(self):
        self.running = True
        for i in range(50000):
            print("está contando", i)
        self.running = False

    def check_thread(self):
        if self.running:
            self.after(1000, self.check_thread) # run again after 1s (1000ms)
        else:
            print('stop')
            self.windows_bar.progressbar.stop()
            self.windows_bar.destroy()
            self.button.config(state=tk.NORMAL)
        
        
class WinProgressBar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Barr progress")
        self.geometry("300x200")
        self.progressbar = ttk.Progressbar(self, mode="indeterminate")
        self.progressbar.place(x=30, y=60, width=200)
        self.progressbar.start(20)


if __name__ == "__main__":
    app = App()
    app.mainloop()