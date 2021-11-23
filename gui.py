import PySimpleGUIQt as sg


import platform
import os
import shutil

from PySimpleGUIQt.PySimpleGUIQt import Button


layout = [
    [sg.Button('start')],
    [sg.MultilineOutput()]
]

col1 = [
    [sg.Button('Start')],
    [sg.Button('Settings'), [sg,Button('')]],
]

layout1 = [
    [sg.Text('TR')],
    
]

window = sg.Window('TR', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'start':
        import main
        main


window.close()