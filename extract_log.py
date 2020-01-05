#!/usr/bin/python

import pandas as pd
import sys
import os
import sys
import PySimpleGUI as sg
import subprocess
import pyautogui
import codecs
import os
import sys

'''
https://pysimplegui.readthedocs.io/en/latest/cookbook/
https://github.com/PySimpleGUI/PySimpleGUI/issues/850
https://video.online-convert.com/convert-to-mp4
'''

# below line wraps text within the DataFrame
pd.set_option('display.max_colwidth',-1)

#  Function to extract log file based on search string
def extract_log_file(l_file,search_string):
    try:
        logfile = codecs.open(l_file, encoding='utf-8')
        c = 0
        count = []
        log = []
        for lines in logfile:
            l = lines.replace(chr(10),"").replace('\n',"")
            c += 1
            search_string = search_string.strip()
            search_string = " " + search_string + " "
            if search_string.lower() in str(l).lower():
                log.append(l)
                count.append(c)
        df = pd.DataFrame({"Line Number":count,"Lines":log})
        df['Lines'] = df['Lines'].str.wrap(100)
        print (df)
    except Exception as e:
        print('\nSearch string Not Found in the file OR File not selected')
        print('\n' + str(e))

#extract_log_file('E:\myproj\desktop_ui\syslog','origin')

sg.theme('BluePurple')

layout = [
    [sg.Text('Click Browse button to select the log file :-', size=(40, 1))],
    [sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False)],
    [sg.FileBrowse(target='_FILEBROWSE_')],
    [sg.Text('Enter Search string below:')],
    [sg.InputText(size=(50,1))],
    [sg.Output(size=(150, 20))],
    [sg.Button('RUN'), sg.Button('CLEAR'),sg.Text('(CLICK INSIDE SEARCH / OUTPUT WINDOW & CLICK CLEAR BUTTON)', size=(61, 1)), sg.Button('EXIT')]
]

window = sg.Window('Log File Extractor',layout)

while True:
    e,v = window.read()
    # print(v[0])
    # print(v['Browse'])
    if e == 'EXIT' or e is None:
        break
    elif e == 'RUN':
        extract_log_file(v['Browse'],v[0])
    elif e == 'CLEAR':
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('del')

