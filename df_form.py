#!/usr/bin/python

import PySimpleGUI as sg
import pandas as pd
import webbrowser

sg.theme('BlueMono')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please Fill the form to create DataFrame')],
    [sg.Text('Region', size=(15, 1)), sg.InputText()],
    [sg.Text('Company', size=(15, 1)), sg.InputText()],
    [sg.Text('Product', size=(15, 1)), sg.InputText()],
    [sg.Text('Month', size=(15, 1)), sg.InputText()],
    [sg.Text('Sales', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Exit()]
]
window = sg.Window('DataFrame Form Builder', layout)

r,c,p,m,s = [],[],[],[],[]
while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if event == 'Submit':
        r.append(values[0]),c.append(values[1]),p.append(values[2]),m.append(values[3]),s.append(values[4])
        [window[i]('') for i in range(0,len(values))]

df = pd.DataFrame({'Region':r,'Company':c,'Product':p,'Month':m,'Sales':s})
df.to_html('df.html')
if len(df) > 0:
    webbrowser.open('df.html')