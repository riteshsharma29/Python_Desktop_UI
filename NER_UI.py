import PySimpleGUI as sg
import spacy
from spacy import displacy
from tkhtmlview import HTMLLabel
import webbrowser
import codecs

"""
Install all dependencies using pip
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download nl_core_news_sm
python -m spacy download en_core_web_sm
python -m spacy download fi_core_news_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm
python -m spacy download es_core_news_sm
python -m spacy download sv_core_news_sm
pip install PySimpleGUI
pip install tkhtmlview
"""

def Ner_func_2(lang_core,raw_text):
    try:
        NER = spacy.load(lang_core)
        text1 = NER(raw_text)
        svg = displacy.render(text1, style="ent", page=True)
        layout = [[]]
        new_window = sg.Window('NER VISUALIZATION', layout, finalize=True)
        my_label = HTMLLabel(new_window.TKroot, html=svg)
        f = codecs.open("output.html","w",encoding="utf-8")
        f.write(svg)
        for word in text1.ents:
            print(word.text, word.label_)
        my_label.pack()
    except Exception as err:
        print(err)

# languages list
input_lang = [
    'English',
    'Dutch',
    'Finnish',
    'French',
    'German',
    'Spanish',
    'Swedish',
]

# GUI color
sg.theme('BluePurple')

# UI layout
layout = [
    [
        sg.Submit('CLEAR INPUT', size=(24, 1)),
        sg.Submit('CLEAR OUTPUT', size=(24, 1)),
        sg.Submit('RUN NER', size=(24, 1)),
        sg.Submit('EXIT', size=(24, 1))

    ],
    [
        sg.Radio('NONE', "RADIO1",size=(5, 5),font=("Helvetica", 15), default=True),
        sg.Radio('English', "RADIO1",size=(6, 5),font=("Helvetica", 15), default=False, key="-eng-"),
        sg.Radio('Dutch', "RADIO1",size=(6, 5),font=("Helvetica", 15), default=False,key="-dut-"),
        sg.Radio('Finnish', "RADIO1",size=(6, 5),font=("Helvetica", 15), default=False, key="-fin-"),
        sg.Radio('French', "RADIO1",size=(6, 5),font=("Helvetica", 15), default=False, key="-fre-"),
        sg.Radio('German', "RADIO1",size=(7, 5),font=("Helvetica", 15), default=False, key="-ger-"),
        sg.Radio('Spanish', "RADIO1",size=(7, 5),font=("Helvetica",15), default=False, key="-esp-"),
        sg.Radio('Swedish', "RADIO1",size=(7, 5),font=("Helvetica", 15), default=False, key="-swe-"),

    ],
    [
        sg.Text('INPUT TEXT                    ', size=(20, 1)),
        sg.Multiline(size=(59, 10),font=("Helvetica", 15), key='Input')
    ],
    [
        sg.Text('NER OUTPUT                          ', size=(20, 1)),
        sg.Output(size=(59, 10), font=("Helvetica", 15),key='Output')],
]

window = sg.Window('MULTILINGUAL NER - NAMED ENTITY RECOGNITION INTERFACE', layout, resizable=True)


# UI functionality
while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'EXIT':
        break
    # calling respective NER language function
    elif v["-eng-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-dut-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-fin-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-fre-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-ger-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-esp-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif v["-swe-"] == True and e == 'RUN NER' and len(v['Input']) > 0:
        Ner_func_2("en_core_web_sm",v['Input'])
        webbrowser.open_new_tab("output.html")
    elif e == 'CLEAR INPUT':
        window['Input'].Update('')
    elif e == 'CLEAR OUTPUT':
        window['Output'].Update('')
