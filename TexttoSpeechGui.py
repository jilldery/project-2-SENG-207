import pyttsx3
import PySimpleGUI as sg

layout = [
    [sg.Text('Please enter text:', background_color='yellow', text_color='black')],
    [sg.Input()],
    [sg.Radio('Female voice', 'VOICE', key='female', default=True, background_color='yellow', text_color='black'),
     sg.Radio('Male voice', 'VOICE', key='male', background_color='yellow', text_color='black')],
    [sg.Button('Speak', button_color=('white', 'blue'))]
]

window = sg.Window('Text to Speech', layout, background_color='yellow')

engine = pyttsx3.init()


def speak(text, voice):
    if voice == 'male':
        engine.setProperty('voice', 'english+m7')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', 1.0)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    elif voice == 'female':
        engine.setProperty('voice', 'english+f4')
        engine.setProperty('rate', 100)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()


while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Speak':
        text = value[0]
        if value['female'] == True:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
        elif value['male'] == True:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()



