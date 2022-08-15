#!/usr/bin/python

import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect('employee.db')
cur = conn.cursor()

def insert(*args):
    reclist = list(args)
    cur.execute('SELECT * FROM `employee` where  `name` = "' + reclist[1] + '";')
    if cur.fetchone() == None:
        # Constructing insert query
        insert_query = ''
        insert_query += 'insert INTO employee VALUES ('
        for iqi in range(0,6):
            reclist[iqi] = str(reclist[iqi])
            insert_query += chr(34) + reclist[iqi].strip() + chr(34) + ","
        insert_query = insert_query[:-1]
        insert_query += ");"
        print(insert_query)
        cur.execute(insert_query)
        conn.commit()
        sg.popup("CREATE QUERY",'RECORDS FOR ID :' + str(reclist[0]) + ' ADDED IN THE DATABASE')
    else:
        sg.popup("CREATE QUERY",'RECORDS FOR ID :' + str(reclist[0]) + ' ALREADY EXISTS IN THE DATABASE')

def delete(namevar):
    cur.execute('DELETE FROM `employee` where Name="' + namevar + '";')
    conn.commit()
    sg.popup("DELETE QUERY",'RECORDS FOR NAME :' + namevar + ' DELETED FROM THE DATABASE')

def update(namevar):
    records = cur.execute('SELECT * FROM `employee` where Name="' + namevar + '";')
    records = records.fetchall()
    return records

def modify(*args):
    reclist = list(args)
    col_list = ["empid","name","email","gender","department","date_of_joining"]
    cur.execute('SELECT * FROM `employee` where  `name` = "' + reclist[6] + '";')
    if cur.fetchone() != None:
        # Constructing update query
        update_query = ''
        update_query += 'UPDATE `employee` SET '
        for iqi in range(0, 6):
            reclist[iqi] = str(reclist[iqi])
            update_query += "`" + col_list[iqi] + "`=" + chr(34) + reclist[iqi].strip() + chr(34) + ","
        update_query = update_query[:-1]
        update_query += ' WHERE `Name` = ' + chr(34) + reclist[6] + chr(34) + ";"
        # print(update_query)
        cur.execute(update_query)
        conn.commit()
        sg.popup("UPDATE QUERY",'RECORDS FOR NAME :' + reclist[1] + ' UPDATED IN THE DATABASE' + '\n\n' + 'PLEASE CLICK CLEAR BUTTON')


sg.theme('TanBlue')
window = sg.Window('Window Title', location=(0,0), size=(800,600), keep_on_top=True)

layout = [
[sg.Text('EMPLOYEE ID :', font=('Arial', 10, 'bold')),sg.InputText(size=(22, 2),key='eid')],
    [sg.Text('NAME        :', font=('Arial', 10, 'bold')),sg.InputText(size=(25, 2),key='name')],
    [sg.Text('EMAIL       :', font=('Arial', 10, 'bold')),sg.InputText(size=(25, 2),key='email')],
    [sg.Text('GENDER:    ', font=('Arial', 10, 'bold')), sg.Combo(
        [
            'MALE',
            'FEMALE',
        ], size=(24, 8), key='gender')
     ],
    [sg.Text('DEPARTMENT:', font=('Arial', 10, 'bold')), sg.Combo(
        [
            'ACCOUNTS',
            'HR',
            'OPERATIONS',
            'SOFTWARE',
            'ADMIN'],size=(22,8),key='depart')
     ],
    [sg.Text('DATE OF JOINING', key='-CALOUTPUT-', font=('Arial', 10, 'bold')),
     sg.InputText(key='-CAL-', size=(20, None), font=('Arial', 10, 'bold'))],
    [sg.CalendarButton('SELECT DATE', target='-CAL-', pad=None, font=('Arial', 10, 'bold'), format='%m/%d/%Y')],
    [sg.Text('NOT FOR USER:', font=('Arial', 10, 'bold'),text_color="red"), sg.InputText(size=(22, 2), key='not_for_user')],
    [sg.Submit('ADD RECORD',size=(15,3)),sg.Submit('SEARCH',size=(15,3)),sg.Submit('MODIFY RECORD',size=(15,3)),sg.Submit('DELETE RECORD',size=(15,3)),sg.Submit('CLEAR',size=(10,3)),sg.Submit('EXIT',size=(10,3))],
 ]

window = sg.Window('CRUD SQLITE3 GUI', layout,resizable=True, finalize=True)

while True:
    # e stands for events, v stands for values
    e, v = window.read()
    if e is None or e == 'EXIT':
        break
    #  calling add function and clicking this button to add records
    elif e == 'ADD RECORD':
        insert(v['eid'],
               v['name'],
               v['email'],
               v['gender'],
               v['depart'],
               v['-CAL-']
               )
    #  calling delete function and clicking this button to delete records
    elif e == 'DELETE RECORD':
        delete(v['name'])
    elif e == 'SEARCH':
        try:
            # calling update function with Name parameter
            rec = update(v['name'].strip())
            #  populating all the fields from above tuple ie rec
            window['eid'].Update(rec[0][0])
            window['name'].Update(rec[0][1])
            window['email'].Update(rec[0][2])
            window['gender'].Update(rec[0][3])
            window['depart'].Update(rec[0][4])
            window['-CAL-'].Update(rec[0][5])
            window['not_for_user'].Update(rec[0][1])
        except:
            sg.popup('RECORDS FOR NAME :' + v['name'] + ' DOES NOT EXISTS IN THE DATABASE')
    elif e == 'MODIFY RECORD':
        modify(v['eid'],
               v['name'],
               v['email'],
               v['gender'],
               v['depart'],
               v['-CAL-'],
               v['not_for_user'])
    elif e == 'CLEAR':
        window['eid'].Update('')
        window['name'].Update('')
        window['email'].Update('')
        window['gender'].Update('')
        window['depart'].Update('')
        window['-CAL-'].Update('')
        window['not_for_user'].Update('')
