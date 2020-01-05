#!/usr/bin/python

import PySimpleGUI as sg
import pandas as pd
import webbrowser

sg.theme('Dark Blue 3')      # Add some color to the window
df = pd.read_excel('links.xlsx')
links = df['URL'].to_list()


layout = [
    [sg.InputCombo(links, default_value='SELECT', size=(75, 200), font=("Helvetica", 15), text_color='blue')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('PLEASE SELECT THE URL FROM DROPDOWN LIST', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if values[0] == 'SELECT' or type(values[0]) == 'Nonetype':
        sg.popup('ERROR !!!','URL NOT SELECTED','PLEASE SELECT URL AND THEN CLICK SUBMIT BUTTON')
    if event == 'Submit' and values[0] != 'SELECT':
        webbrowser.open(values[0])


