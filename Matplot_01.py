#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:25:19 2022

@author: antoiovi
"""

from calendar import firstweekday

import pandas as pd
import numpy as np


import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import BOTH, ttk

import logging
logger = logging.getLogger(__name__)

class Dialog(tk.Toplevel):
 def __init__(self, parent,message):
        super().__init__(parent)
        text_box = tk.Text(self)
        text_box.pack(fill=tk.BOTH)
        text_box.config(state='normal')
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, message)
        text_box.config(state='disabled')

    
class ReportNotes(tk.Frame):
    def handle_double_click(self,event):
        msg= self.text_box.get("1.0",tk.END)
        dialog =Dialog(self,message=msg) #Here
        return 

            
    def set_message(self,message):
        self.text_box.config(state='normal')
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, message)
        self.text_box.config(state='disabled')

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent,  width=100, height=60,*args, **kwargs)
        
        self.text_box = tk.Text(self)
        self.text_box .bind("<Double-1>", self.handle_double_click)
        ys = ttk.Scrollbar(self, orient = 'vertical', command = self.text_box.yview)
        xs = ttk.Scrollbar(self, orient = 'horizontal', command = self.text_box.xview)
        self.text_box['yscrollcommand'] = ys.set
        self.text_box['xscrollcommand'] = xs.set
        self.text_box.insert('end', ".......\n...\n...")
        self.text_box.grid(column = 0, row = 0, sticky = 'nwes')
        xs.grid(column = 0, row = 1, sticky = 'we')
        ys.grid(column = 1, row = 0, sticky = 'ns')
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_propagate(False)

class Frame_plot(tk.Frame,Observer):
    LARGHEZZA=13
    ALTEZZA=6
    
    selectedStation=""
    selectedSensor=""
    selectedDateFrom=""
    selectedDateTo=""
    
    def set_note(self,msg):
        if msg is None:
            msg=" "
        self.report_notes.set_message(msg)
        #self.label_notes.config(text = msg)
        
    def update(self,program_event):
        logger.debug(program_event)
    

    def onclick(self,event):
          '''
        dfi[ 'station', 'date', 'note', 'ticket', 'date_open', 'date_close',
          'canale', 'tipo', 'val_teorico', 'Val_lettura', 'ora1', 'ora2']
      dfi.index =  RangeIndex(start=0, stop=nnn, step=1
          '''
          '''TODO Click sul canvas non fa' ancora nulla'''
          d=matplotlib.dates.num2date(event.xdata, tz=None)
          return
          x=self.filteredDfi[self.filteredDfi['date']==d.date()]
          
          if x.empty:
              return
              print("ONCLICK : VUOTO")
              print(x)
          else:
              return
              print("NON VUOTO")
              print(x)


    def on_move(self,event):
            # get the x and y pixel coords
            x, y = event.x, event.y
            if event.inaxes:
                ax = event.inaxes  # the axes instance
                #print('data coords %f %f' % (event.xdata, event.ydata))
                try:
                    #print("Try.....")
                    d=matplotlib.dates.num2date(event.xdata, tz=None)
                    if self.dfinterventi is None:
                        logger.debug("dfinterventi is None")
                        return
                    df_interventi=self.dfinterventi
                    
                    df_interventi['date2']=df_interventi['date'].apply(lambda x: x.date())
                    dati_punto_XY=df_interventi[df_interventi['date2']==d.date()]
                
                    if dati_punto_XY.empty:
                        #print("VUOTO")
                        self.annot.set_visible(False)
                        self.figura.canvas.draw_idle()
                        self.set_note((" "))
                        
                    else:
                        #print("Non vuoto")
                         #names=['station','date','note','ticket','date_open','date_close','canale','tipo','val_teorico','Val_lettura','ora1','ora2']
                        testo=self.selectedStation +" "+ self.selectedSensor+"\n"
                        testo2=self.selectedStation +" "+ self.selectedSensor+"\n"
                        
                        note="Note : \n"
                        for i,r in dati_punto_XY.iterrows():
                            testo=testo+str(r['date2'])+" tipo :"+r['tipo']+" "+r['canale'] + str(r['Val_lettura'])+"\n"
                            testo2=testo2+str(r['date2'])+" tipo :"+r['tipo']+" "+r['canale'] + str(r['Val_lettura'])
                            # ps.isnul() invece di np.isnan() perche con stringa non funziona
                            n= '---' if pd.isnull(r['note']) else r['note']
                            note=note+r['tipo']+" "+r['canale'] +" : "+ n+"; \n "#+"\n"
                            testo2=testo2+" Note :"+n+"\n"
                            #testo=testo+str(r['date']) +"tipo :"+r['tipo']+" "+r['canale']+"\n"
                        #print(testo2)
                        # Aggiorna la casella di testo SOVRAPPOSTA al grafico
                        self.update_annot(event.xdata,event.ydata,testo)
                        self.annot.set_visible(True)
                        # Aggiorna il text box sotto il grafico
                        self.set_note(testo2)
                        self.figura.canvas.draw_idle()
                except matplotlib.units.ConversionError as e:
                    logger.critical("matplotlib.units.ConversionError ")
                    self.annot.set_visible(False)
                    self.figura.canvas.draw_idle()
                except Exception as e:
                    logger.error('Errore... ', exc_info=e)
                    
    def update_annot(self,x,y,testo):
        try:
            self.annot.xy = (x,y)
            text = testo
            self.annot.set_text(text)
            self.annot.get_bbox_patch().set_alpha(0.4)
        except Exception as e:
            logger.error('Errore updating annotation... ', exc_info=e)

    def __init__(self, parent,programma, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.container=ttk.Frame(self)
        self.container.grid(column=0, row=0)
        
        self.dfinterventi=None
  
        fig = Figure(figsize=(self.LARGHEZZA,self.ALTEZZA), dpi=100)
        self.figura=fig
        ax=fig.add_subplot(111)
        self.asse=ax
        
        self.canvas = FigureCanvasTkAgg(fig, master=self.container)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=5)
        
        self.canvas.mpl_connect('button_press_event', self.onclick)
        self.canvas.mpl_connect('motion_notify_event', self.on_move)

        toolbar = NavigationToolbar2Tk(self.canvas, self.container)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.report_notes=ReportNotes(self.container)
        self.report_notes.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=2)
        
    def clear_plot(self):
        self.asse.clear()
    
    
    def annotation_create(self):
        '''
        L'annotation deve essere creata ogni volta che si fa il clear degli 
        assi .

        Returns
        -------
        annotation

        '''
        self.annot=self.asse.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)
        return self.annot

    

    def plot_data(self,programma):
       
       self.selectedStation=programma.selectedStation # Servono per annotation
       self.selectedSensor=programma.selectedSensor
       datiXY=programma.get_data_to_plot()
       self.annot=self.annotation_create()
       if datiXY is None:
           return
       x=programma.get_data_to_plot()[0]
       y=programma.get_data_to_plot()[1]
       Max=datiXY[2]
       Min=datiXY[3]
       Std=datiXY[4]
       
       '''
            ANNOTAZIONE DA RENDERE VISIBILE QUANDO PASSO IL MOUSE SOPRA 
            (hover annotation  evento on_move)
      '''        
       
       logger.debug("Plotting x e y")

       linesnames=['Mediamobile','Max','Min','stdband','std']

       for t in programma.linestoplot:
            if t[0]==linesnames[0]:
                if t[1]==1:
                    self.asse.plot(x,y,  c='b', label='mean',linewidth=1.0)
            elif t[0]==linesnames[1]:
                if t[1]==1:
                    self.asse.plot(x,Max,  c='gray', label='max',linewidth=1.0)
            elif t[0]==linesnames[2]:
                if t[1]==1:
                    self.asse.plot(x,Min,  c='gray', label='min',linewidth=1.0)
            elif t[0]==linesnames[3]:
                if t[1]==1:
                    sup=y+Std
                    inf=y-Std
                    self.asse.plot(x,sup,  c='y', label='stdband',linewidth=1.0)
                    self.asse.plot(x,inf,  c='y', label='stdband',linewidth=1.0)
                    
            elif t[0]==linesnames[4]:
                if t[1]==1:
                    self.asse.plot(x,Std,  c='y', label='std',linewidth=1.0)
            else:
                   self.asse.plot(x,y,  c='b', label='mean',linewidth=1.0)
       
       
       d=programma.selectedDateFrom
       dal="{}-{}-{}".format(d.day,d.strftime("%B"),d.year)
       d=programma.selectedDateTo
       al="{}-{}-{}".format(d.day,d.strftime("%B"),d.year)
       
       titolo='Stazione: {} Sensore {}\n dal {} al {} \n media mobile {}'.format(
           self.selectedStation,self.selectedSensor,dal,al,programma.mediamobile)

       self.asse.set_title(titolo,fontsize = 12)
       self.canvas.draw()
    
    
    def plot_interventi(self,programma):
        '''
        Filtra il dataframe intereventi in base self.selectedStation,...
        

        Returns
        -------
        None.

        '''
        self.dfinterventi=programma.selectedDataI.dfi
        if self.dfinterventi is None:
            self.set_note("Nessun intervento presente o selezionato.")
            return
        dati=programma.get_vlines_to_plot()
        if dati is None :
            self.set_note("Nessun intervento presente o selezionato.")
            return
        datei=dati['date_interventi']
        tarature=dati['tarature']
        
        tarature=tarature.set_index('date')
        #print(tarature)
        #-------------------------------------------------------
        # Plotto le linee verticali per le date degli interventi
        #-------------------------------------------------------
        for d in datei:
            #print(d)
            if d in tarature.index:
                self.asse.axvline(x=d,color='g')
            else:
                self.asse.axvline(x=d,color='r')
                
        self.canvas.draw()
