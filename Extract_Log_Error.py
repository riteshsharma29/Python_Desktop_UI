import pandas as pd
import PySimpleGUI as sg
import codecs

# below line wraps text within the DataFrame
pd.set_option('display.max_colwidth',None)

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
            search_string = str(search_string).strip()
            if search_string.lower() in str(l).lower():
                log.append("                        " + l)
                count.append(c)
        df = pd.DataFrame({"Line Number":count,"Lines":log})
        df.to_excel("extract.xlsx",index=False)
        df['Lines'] = df['Lines'].apply(str).str.wrap(100)
        print ("################### LOG EXTRACT OF FILE : " + str(l_file) + " ######################\n\n",df.to_string(index=False))
    except Exception as e:
        print('\nSearch string Not Found in the file OR File not selected')
        print('\n' + str(e))

# extract_log_file('F:\\myprojects\\fast_api_prac\\sql_app\\requirements.txt','https')

sg.theme('BluePurple')

layout = [
    [
        sg.Text('Click Browse button to select the log file :-', size=(40, 1))
    ],
    [
        sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False)
    ],
    [
        sg.FileBrowse(target='_FILEBROWSE_')
    ],
    [
        sg.Text('Enter Search string below:')
    ],
    [
        sg.InputText(size=(50,1))
    ],
    [
        sg.Output(size=(150, 20),key='ouput')
    ],
    [
        sg.Button('RUN'),
        sg.Button('CLEAR'),
        sg.Button('EXIT')]
]

window = sg.Window('LOG ERROR EXTRACTOR (Extracted report gets saved as extract.xlsx)',layout,resizable=True, finalize=True)

# Functionality
while True:
    e,v = window.read()
    # print(v[0])
    # print(v['Browse'])
    if e == 'EXIT' or e is None:
        break
    elif e == 'RUN':
        extract_log_file(v['Browse'],v[0])
    elif e == 'CLEAR':
        window['ouput'].Update('')