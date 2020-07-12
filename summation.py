import PySimpleGUI as sg
sg.theme('LightGrey')
layout = [
    [sg.Text('Enter Numbers', size=(10, 1)),sg.InputText(size=(10,2),background_color='lightblue',key='input_1'),sg.Text('+', size=(2, 1)),
	sg.InputText(size=(10,2),background_color='lightblue',key='input_2'),sg.Button('Calculate', size=(10, 2))
	],
	[sg.Text('Result : -->', size=(10, 1)),	sg.Output(size=(15, 5), font=("Helvetica", 15),key='output'),
	sg.Button('Quit', size=(10, 2))],
	[sg.Submit('CLEAR', size=(50, 2))]
]
window = sg.Window('SUM EXAMPLE',layout)
while True:
    e,v = window.read()
    if e is None or e == 'Quit':
        break
    elif e == 'CLEAR':
        window['output'].Update('')
        window['input_1'].Update('')
        window['input_2'].Update('')
    elif e == 'Calculate':
        print(int(v['input_1']) + int(v['input_2']))