import paramiko
import PySimpleGUI as sg
import os

def Prerequisites():
    print('1.Requires ssh/openssh enabled Remote Target Linux Server\n')
    print('2. Test ssh connection to the Linux Server using putty client if required. \n')
    print('3. Install module (PySimpleGUI,paramiko) dependencies using pip\n')
    print('4. Use base64 encrypted password. Command example mentioned below :\n')
    print('5. echo Your_Linux_Password_without_any_quotes | c:\python39\python.exe -m base64  -e\n')
    print('6. Extract Log files, Configuration files etc. ')

def extract_log_file(hostname,username,passwd,filepath):
    try:
        client = paramiko.SSHClient()
        # decoding base64 encoded password
        dec_pass = os.popen(" echo " + passwd + " | c:\python39\python.exe -m base64  -d").read()
        dec_pass = dec_pass.strip(' \n')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, username=username, password= dec_pass)
        stdin, stdout, stderr = client.exec_command('cat ' + filepath)
        for line in stdout:
            print(line.strip('\n'))
        client.close()
    except Exception as e:
        print(e)


# GUI color
sg.theme('BluePurple')

# GUI layout
layout = [
    [
        sg.Text('HOST'), sg.InputText(size=(25, 10), key='host'),
        sg.Text('USER'), sg.InputText(size=(25, 10), key='user'),
        sg.Text('PASSWORD'), sg.InputText(size=(25, 10), key='password'),
        sg.Text('FILEPATH'), sg.Multiline(size=(35, 1), key='fpath')

    ],
    [
        sg.Output(size=(150, 30),key='ouput')
    ],
    [
        sg.Button('HELP'),
        sg.Button('CLEAR OUTPUT WINDOW'),
        sg.Button('RUN'),
        sg.Button('RESET'),
        sg.Button('CLEAR FILEPATH'),
        sg.Button('EXIT')
    ]
]

window = sg.Window('LINUX SERVER FILE EXTRACTOR',layout,resizable=True, finalize=True)

# GUI functionality
while True:
    e,v = window.read()
    if e == 'EXIT' or e is None:
        break
    elif e == 'RUN' and v['host'] != 0 and v['user'] != 0 and v['password'] != 0 and v['fpath'] != 0:
        # Call Function
        extract_log_file(v['host'], v['user'], v['password'], v['fpath'])
    elif e == 'HELP':
        Prerequisites()
    elif e == 'CLEAR FILEPATH':
        window['fpath'].Update('')
    elif e == 'CLEAR OUTPUT WINDOW':
        window['ouput'].Update('')
    elif e == 'RESET':
        window['host'].Update('')
        window['ouput'].Update('')
        window['user'].Update('')
        window['password'].Update('')
        window['fpath'].Update('')