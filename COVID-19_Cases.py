# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:06:41 2020

@author: Adam-22-26
"""


import tkinter 
from tkinter import *
import tkinter.ttk as tk
import pandas as pd
#from datetime  import datetime, timedelta
#from matplotlib import dates as mpl_dates
import csv
import tkinter as tk

from tkinter import *
#from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.dates import MonthLocator, DateFormatter


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure

mainwindow = Tk()
mainwindow.geometry('1000x800')
mainwindow.title('COVID-CASES')
#mainwindow.resizable(False, False)

frametop = LabelFrame(mainwindow, width = 860,height = 230, text = "PATIENT PERSONAL DATA", bd = 3)
frametop.pack(side = TOP, fill ='both', expand='yes')

framebot = LabelFrame(mainwindow, width = 860,height = 230, text = "GRAPHS HERE", bd = 3)
framebot.pack(side =BOTTOM,  fill ='both', expand='yes')


# LABEL
names = tk.Label(frametop, width = 10, text ='CASE ID:')
names.place(x = 10, y = 40)
name = tk.Entry(frametop, width = 40)
name.place(x = 80, y = 40)

address = tk.Label(frametop, width = 10, text ='RESIDENCE  :')
address.place(x = 10, y = 80)
add = tk.Entry(frametop, width = 40, text = 'Province in China')
add.place(x = 80, y = 80)

ages = tk.Label(frametop, width = 10, text ='AGE   :')
ages.place(x = 10, y = 120)
age = tk.Entry(frametop, width = 10)
age.place(x = 80, y = 120)

bloodtype = tk.Label(frametop, width = 10, text ='BLOOD   :')
bloodtype.place(x = 180, y = 120)
blood = tk.Entry(frametop, width = 11)
blood.place(x = 250, y = 120)

stat = Label(frametop, text = 'STATUS   :')
stat.place(x = 10, y = 180)
positive = IntVar()
post = Checkbutton(frametop, text = "POSITIVE", variable = positive, onvalue = 1, offvalue = 0, height=1, width = 6)
post.place(x = 80, y = 150)

pui = IntVar()
Pui = Checkbutton(frametop, text = "PUI", variable = pui, onvalue = 1, offvalue = 0, height=1, width = 6)
Pui.place(x = 65, y = 180)

pum = IntVar()
Pum = Checkbutton(frametop, text = "PUM", variable = pum, onvalue = 1, offvalue = 0, height=1, width = 6)
Pum.place(x = 69, y = 210)


dt = tk.Label(frametop, width = 10, text ='MM/DD/YY :')
dt.place(x = 180, y = 150)
date = Entry(frametop, width = 11)
date.place(x= 250, y = 150)

#-----------------------------------------------------------------------

confirm = Label(frametop,text = 'CONFIRM CASES')
confirm.place(x = 150, y = 300)



def SAVE():
    Name = name.get()
    Address = add.get()
    Age = age.get()
    Blood = blood.get() 
    pos = positive.get()
    pos = str(pos)
    Pui = pui.get()
    Pui = str(Pui)
    Pum = pum.get()
    Pum = str(Pum)
    date1 = date.get()
    filename = 'Master_List_cases.csv'
    file = open('Master_List_cases.csv', 'a')
    headers = 'Name,Address,Age,Blood,Positive,PUI,PUM,Date\n'    
    file.write(headers)
    
    file.write(Name + ',' + Address + ','+ Age + ',' + Blood + ',' + pos + ','+ Pui + ',' + Pum + ',' + date1 +'\n')
    
    name.delete(0, 'end')
    add.delete(0, 'end')
    age.delete(0, 'end')
    blood.delete(0, 'end')
    date.delete(0,'end')
    file.close() 
           

save = ttk.Button(frametop, width = 10, text = 'CONFIRM', command = SAVE)
save.place(x = 80, y = 250)
refresh = ttk.Button(frametop, width = 10, text = 'REFRESH')
refresh.place(x =170, y = 250)
char = ttk.Button(frametop, width = 10, text = 'CHART')
char.place(x =255, y = 250)




#-----------------------------------------------------------------------
tkcanvas = plt.Figure(figsize=(6,3), dpi=100) #lines sizes

subplt1 = tkcanvas.add_subplot(111) 
#subplt1.style.use('dark_background')
date2 = FigureCanvasTkAgg(tkcanvas, frametop) #set to the frame

date2.get_tk_widget().pack(side=RIGHT, fill=tk.BOTH) # packing


data1 = pd.read_csv('Master_List_cases.csv')
data1['Date'] = pd.to_datetime(data1['Date'])
data1.sort_values('Date', inplace=True)
data1 = data1[['Date','Positive']].groupby('Date').sum() # # legent
data1.plot(kind='line', legend=True, ax=subplt1, color='red',marker='.', fontsize=6)
data1.style.use('dark_background')

data2 = pd.read_csv('Master_List_cases.csv')
data2['Date'] = pd.to_datetime(data2['Date'])
data2.sort_values('Date', inplace=True)
data2 = data2[['Date','PUI']].groupby('Date').sum() # # legent
data2.plot(kind='line', legend=True, ax=subplt1, color='orange',marker='o', fontsize=6, linestyle='-.')
data2.style.use('dark_background')

data3 = pd.read_csv('Master_List_cases.csv')
data3['Date'] = pd.to_datetime(data3['Date'])
data3.sort_values('Date', inplace=True)
data3 = data3[['Date','PUM']].groupby('Date').sum() # # legent
data3.plot(kind='line', legend=True, ax=subplt1, color='green',marker='*', fontsize=6, linestyle='--')
data3.style.use('dark_background')

subplt1.grid(color='r', linestyle='-', linewidth=0.050)
subplt1.set_title('PERSON IN LINE')
subplt1.set_ylabel('COUNT')

#--------------------------------------------------------------------------------------------------

ads = pd.read_csv('Master_List_cases.csv')

barfig = plt.Figure(figsize=(10,3), dpi=100)
barx = barfig.add_subplot(111)
placebar = FigureCanvasTkAgg(barfig, framebot)
placebar.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
ads = ads[['Address','Positive']].groupby('Address').sum()
ads.plot(kind='bar', legend=True, ax=barx ,fontsize=7)
barx.set_title('Places with Infected')
barx.set_ylabel('Total Confirmed Cases')
barx.set_xlabel('Places')
#print(plt.style)




mainwindow.mainloop()