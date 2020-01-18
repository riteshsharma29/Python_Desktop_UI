#!/usr/bin/python

import PySimpleGUI as sg
import re


def Match_regex(pattern, text):
    try:
        pattern = pattern.lstrip().rstrip()
        match = re.findall(pattern, text)
        regex = re.compile(pattern)
        match_iter = re.finditer(pattern, text)
        print(match)
    #     for match in match_iter:
    #         print (match.group())
    #         print('Match Found. Text: {0} Index: {1} Length: {2}'.format(text, match.start(),len(match.group(0))))
    #         for i in range(0,len(match.group())):
    #             gn = i + 1
    #             group_name = None
    #             regex_group_index = dict((v,k) for k,v in regex.groupindex.items())
    #             if gn in regex_group_index:
    #                 group_name = regex_group_index[gn]
    #             print('  Group:{0}, Name:{1}, Value: {2}'.format(gn, group_name, match.group(gn)))
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


def Split_regex(pattern, text):
    try:
        pattern = pattern.strip()
        text = text.strip()
        split_text = re.split(pattern, text)
        if len(split_text) > 0: print('Splitted Text:')
        for s in split_text:
            print('{0}'.format(s))
    except Exception as e:
        print(e)


# UI layout
layout = [
    [sg.Text('Pattern                    ', size=(20, 1)), sg.InputText(size=(60, 60), key='Pattern')],
    [sg.Text('Replacement Text                    ', size=(20, 1)), sg.InputText(size=(60, 60), key='Replacement')],
    [sg.Text('Input Text                    ', size=(20, 1)), sg.Multiline(size=(60, 10), key='Input')],
    [sg.Submit('Match', size=(24, 1)), sg.Submit('Replace', size=(24, 1)), sg.Submit('Split', size=(24, 1))],
    [sg.Text('Result                    ', size=(20, 1)), sg.Output(size=(60, 10), key='Output')],
    [sg.Submit('CLEAR INPUT', size=(24, 1)), sg.Submit('CLEAR OUTPUT', size=(24, 1)),
     sg.Submit('CLEAR ALL', size=(24, 1))],
]

window = sg.Window('Regex Test Tool', layout)

while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'Exit':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'Match' and v['Pattern'] != 0 and v['Input'] != 0:
        Match_regex(r'{}'.format(v['Pattern']), v['Input'])
    elif e == 'Replace' and v['Pattern'] != 0 and v['Replacement'] != 0 and v['Input'] != 0:
        Replace_regex(r'{}'.format(v['Pattern']), v['Replacement'], v['Input'])
    elif e == 'Split' and v['Pattern'] != 0 and v['Input'] != 0:
        Split_regex(r'{}'.format(v['Pattern']), v['Input'])
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
    elif e == 'CLEAR ALL':
        window['Input'].Update('')
        window['Output'].Update('')
        window['Replacement'].Update('')
        window['Pattern'].Update('')
