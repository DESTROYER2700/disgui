# creator: SeaGull aka : DESTROYER2700#6478[]
import PySimpleGUI as sg
import time
import requests 
mk1 = True
sg.theme('DarkAmber')   
layout = [  
            [sg.Text('location'), sg.InputText()],
            [sg.Text('auth token'), sg.InputText()],
            [sg.Text('send'),sg.InputText()],
            [sg.Button('spam'), ] ]


window = sg.Window('SS client', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    location = values[0]
    Auth = values[1]
    msg = values[2]
    payload = {
    'content': msg
    }
    header = {
    'authorization': Auth
    }
    while mk1 == True:
        r = requests.post(location, data=payload, headers=header )
    
    


window.close()