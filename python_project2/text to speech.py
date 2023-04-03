import PySimpleGUI as sg
import pyttsx3
sg.theme('Material2')
engine = pyttsx3.init()
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.InputText()],
    [sg.Text('Volume:'), sg.Slider(range=(0, 100), default_value=50, orientation='h', size=(20, 15), key='-VOLUME-')],
    [sg.Text('Speed:'), sg.Slider(range=(0, 500), default_value=200, orientation='h', size=(20, 15), key='-SPEED-')],
    [sg.Text('Voice:'), sg.Radio('Male', "VOICE", default=True, key='-MALE-'), sg.Radio('Female', "VOICE", key='-FEMALE-')],
    [sg.Button('Speak'), sg.Button('Exit')]
]
window = sg.Window('Text-to-Speech App', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        text = values[0]
        volume = values['-VOLUME-']
        speed = values['-SPEED-']
        voice = 'english+m' if values['-MALE-'] else 'english+f'
        engine.setProperty('rate', speed)
        engine.setProperty('volume', volume/100)
        engine.setProperty('voice', voice)
        engine.say(text)
        engine.runAndWait()
# Cleanup
window.close()