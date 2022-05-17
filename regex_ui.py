#!/usr/bin/python

import PySimpleGUI as sg
import re

def Group(pattern,text,args):
    try:
        pattern = pattern.lstrip().rstrip()
        result = re.match(pattern, text)
        if "," in args:
            args_1 = int(args[0])
            args_2 = int(args[2])
            print(result.group(args_1,args_2))
        elif args == "":
            print(result.groups())
        else:
            args = int(args)
            print(result.group(args))
    except Exception as e:
        print(e)

def Match_regex(pattern, text,args):
    try:
        pattern = pattern.lstrip().rstrip()
        match = re.match(pattern, text)
        if args == "":
            print(match)
        else:
            print(match[int(args)])
    except Exception as e:
        print(e)


def Replace_regex(pattern, replacement_pattern, text):
    try:
        text = str(text).rstrip()
        pattern = pattern.strip()
        new_text = re.sub(pattern, replacement_pattern, text)
        print('New Text:\n{0}'.format(new_text))
    except Exception as e:
        print(e)

def Find_all(pattern,  text):
    try:
        text = str(text).rstrip()
        pattern = pattern.strip()
        new_text = re.findall(pattern, text)
        print('Found Text:\n{0}'.format(new_text))
    except Exception as e:
        print(e)


def Split_regex(pattern, text):
    try:
        pattern = pattern.strip()
        text = text.strip()
        split_text = re.split(pattern, text)
        if len(split_text) > 0: print('Splitted Text:')
        for s in split_text:
            print('{0}'.format(s.strip()))
    except Exception as e:
        print(e)


# UI layout
layout = [
    [
        sg.Text('Pattern                    ', size=(22, 1)), sg.InputText(size=(60, 60), key='Pattern')
    ],
    [
        sg.Text('Replacement Text\Argument                   ', size=(22, 1)), sg.InputText(size=(60, 60), key='Replacement')
    ],
    [
        sg.Text('Input Text                    ', size=(20, 1)), sg.Multiline(size=(60, 10), key='Input')
    ],
    [
        sg.Submit('Match', size=(13, 1)),
        sg.Submit('Replace', size=(13, 1)),
        sg.Submit('Group', size=(13, 1)),
        sg.Submit('Findall', size=(13, 1)),
        sg.Submit('Split', size=(15, 1))
    ],
    [
        sg.Text('Result                    ', size=(20, 1)), sg.Output(size=(60, 10), key='Output')
    ],
    [
        sg.Submit('CLEAR INPUT', size=(17, 1)),
        sg.Submit('CLEAR OUTPUT', size=(18, 1)),
        sg.Submit('CLEAR ALL', size=(18, 1)),
        sg.Submit('EXIT', size=(17, 1))

    ],
]

window = sg.Window('QUICK REGEX TESTING TOOL', layout)

# UI functionality
while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'EXIT':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'Match' and v['Pattern'] != 0 and v['Input'] != 0 and v['Replacement'] != 0 :
        Match_regex(r'{}'.format(v['Pattern']), v['Input'],v['Replacement'])
    elif e == 'Replace' and v['Pattern'] != 0 and v['Replacement'] != 0 and v['Input'] != 0:
        Replace_regex(r'{}'.format(v['Pattern']), v['Replacement'], v['Input'])
    elif e == 'Split' and v['Pattern'] != 0 and v['Input'] != 0:
        Split_regex(r'{}'.format(v['Pattern']), v['Input'])
    elif e == 'Findall' and v['Pattern'] != 0 and v['Input'] != 0:
        Find_all(r'{}'.format(v['Pattern']), v['Input'])
    elif e == 'Group' and v['Pattern'] != 0 and v['Input'] != 0 and v['Replacement'] != 0 :
        Group(r'{}'.format(v['Pattern']), v['Input'],v['Replacement'])
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
    elif e == 'CLEAR ALL':
        window['Input'].Update('')
        window['Output'].Update('')
        window['Replacement'].Update('')
        window['Pattern'].Update('')
