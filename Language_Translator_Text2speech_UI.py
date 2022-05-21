import PySimpleGUI as sg
from mtranslate import translate
from gtts import gTTS
import os
from playsound import playsound

"""
Install all dependencies using pip
pip install PySimpleGUI == 4.47.0
pip install gTTS == 2.2.3
pip install playsound == 1.2.2
"""

# languages list

input_lang = [
    'English',
    'Dutch',
    'French',
    'German',
    'Hindi',
    'Japanese',
    'Kannada',
    'Korean',
    'Polish',
    'Russian',
    'Spanish',
    'Swedish',
    'Tamil',
    'Telugu',
    'Turkish',
    'Ukrainian',
]

input_lang = sorted(input_lang)

# Language ISO codes dict

lang_dict = {
    'English': 'en',
    'Dutch': 'nl',
    'French': 'fr',
    'German':'de',
    'Hindi':'hi',
    'Japanese':'ja',
    'Kannada':'kn',
    'Korean':'ko',
    'Polish':'pl',
    'Spanish':'es',
    'Swedish':'sv',
    'Tamil':'ta',
    'Telugu':'te',
    'Turkish':'tr',
    'Russian':'ru',
    'Ukrainian':'uk',
}

# UI layout
layout = [
    [
        sg.Submit('CLEAR INPUT', size=(24, 1)),
        sg.Submit('CLEAR OUTPUT', size=(24, 1)),
        sg.Submit('CONVERT', size=(24, 1)),
        sg.Submit('PLAY TRANSLATED SPEECH', size=(24, 1))

    ],
    [
        sg.InputCombo(input_lang, default_value='DEFAULT', size=(63, 10), font=("Helvetica", 18))
    ],
    [
        sg.Text('INPUT TEXT                    ', size=(20, 1)),
        sg.Multiline(size=(59, 10),font=("Helvetica", 15), key='Input')
    ],
    [
        sg.Text('TRANSLATED TEXT                    ', size=(20, 1)),
        sg.Output(size=(59, 10), font=("Helvetica", 15),key='Output')],
]

window = sg.Window('LANGUAGE TRANSLATOR WITH TEXT-2-SPEECH UI', layout, resizable=True)


# UI functionality
while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'Exit':
        break
    #  we pass raw string pattern with r'{}'.format(v['Pattern'])
    elif e == 'CONVERT' and v[0] != '' and v[0] != 'DEFAULT' and v['Input'] != 0:
        v['Input'] = v['Input'].strip().replace('\n', " ")
        try:
            if os.path.isfile('lang.mp3') == True:os.remove('lang.mp3')
            print(translate(v['Input'],lang_dict[v[0]]))
            aud_file = gTTS(text=translate(v['Input'],lang_dict[v[0]]), lang=lang_dict[v[0]], slow=False)
            aud_file.save("lang.mp3")
        except Exception as e:
            print(e)
    elif e == 'CONVERT' and v[0] == 'DEFAULT' and v['Input'] != 0:
        try:
            if os.path.isfile('lang.mp3') == True:os.remove('lang.mp3')
            print(translate(v['Input'], 'en'))
            aud_file = gTTS(text=translate(v['Input'], 'en'), lang='en', slow=False)
            aud_file.save("lang.mp3")
        except Exception as e:
            print(e)
    elif e == 'PLAY TRANSLATED SPEECH':
        try:
            playsound('lang.mp3')
        except Exception as e:
            print(e)
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')


