#!/usr/bin/python

import PySimpleGUI as sg
from mtranslate import translate

input_lang = [
    'English',
    'Dutch',
    'French',
    'Spanish',
    'S.Chinese',
    'T.Chinese',
    'German',
    'Hindi',
    'Polish',
    'Tamil',
    'Telugu',
    'Kannada',
    'Russian',
    'Turkish',
    'Danish',
    'Swedish',
    'Korean',
    'Japanese',
]

input_lang = sorted(input_lang)

lang_dict = {
    'English': 'en',
    'Dutch': 'nl',
    'French': 'fr',
    'Spanish':'es',
    'S.Chinese':'zh-CN',
    'T.Chinese':'zh-TW',
    'German':'de',
    'Hindi':'hi',
    'Polish':'pl',
    'Tamil':'ta',
    'Telugu':'te',
    'Kannada':'kn',
    'Russian':'ru',
    'Turkish':'tr',
    'Danish':'da',
    'Swedish':'sv',
    'Korean':'ko',
    'Japanese':'ja',
}

# UI layout
layout = [
    [sg.Submit('CLEAR INPUT', size=(24, 1)), sg.Submit('CLEAR OUTPUT', size=(24, 1)),
     sg.Submit('CONVERT', size=(24, 1))],
    [sg.InputCombo(input_lang, default_value='DEFAULT', size=(40, 10), font=("Helvetica", 18))],
    [sg.Text('INPUT TEXT                    ', size=(20, 1)), sg.Multiline(size=(40, 10),font=("Helvetica", 15), key='Input')],
    [sg.Text('TRANSLATED TEXT                    ', size=(20, 1)), sg.Output(size=(40, 10), font=("Helvetica", 15),key='Output')],
]

window = sg.Window('Language Translation Tool', layout)

while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'Exit':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'CONVERT' and v[0] != '' and v[0] != 'DEFAULT' and v['Input'] != 0:
        v['Input'] = v['Input'].strip().replace('\n', " ")
        #print(v['Input'], lang_dict[v[0]], v[1])
        print(translate(v['Input'],lang_dict[v[0]]))
    elif e == 'CONVERT' and v[0] == 'DEFAULT' and v['Input'] != 0:
        print(translate(v['Input'],'en'))
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
