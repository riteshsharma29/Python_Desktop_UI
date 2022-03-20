#!/usr/bin/python

import PySimpleGUI as sg
import re
import os

'''
Change c:\python39\python.exe below to your python path
'''
def crypto(pattern,method_name):
    try:
        passwd_str = pattern.lstrip().rstrip().strip()
        if method_name == 'ENCRYPT PASSWORD':
            passwd = os.popen(" echo " + passwd_str + " | c:\python39\python.exe -m base64  -e").read()
            print(passwd.strip().strip("\n"))			
        elif method_name == 'DECRYPT PASSWORD':
            passwd = os.popen(" echo " + passwd_str + " | c:\python39\python.exe -m base64  -d").read()			
            print(passwd.strip().strip("\n"))
    except Exception as e:
        print(e)

# UI layout
layout = [
    [sg.Text('Input                     ', size=(20, 1)), sg.Multiline(size=(60, 10), key='Input')],
    [sg.Text('Output                    ', size=(20, 1)), sg.Output(size=(60, 10), key='Output')],
        [sg.Submit('ENCRYPT PASSWORD', size=(38, 1)), sg.Submit('DECRYPT PASSWORD', size=(36,1))],
    [sg.Submit('CLEAR INPUT', size=(24, 1)), sg.Submit('CLEAR OUTPUT', size=(24, 1)),
     sg.Submit('CLEAR ALL', size=(24, 1))],
]

window = sg.Window('Password base64 Encryption/Decryption', layout)

while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'Exit':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'ENCRYPT PASSWORD' and v['Input'] != 0:
        crypto(v['Input'],"ENCRYPT PASSWORD")
    elif e == 'DECRYPT PASSWORD' and v['Input'] != 0:
        crypto(v['Input'],"DECRYPT PASSWORD")
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
    elif e == 'CLEAR ALL':
        window['Input'].Update('')
        window['Output'].Update('')
