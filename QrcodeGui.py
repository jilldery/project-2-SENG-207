import PySimpleGUI as sg
import qrcode



qr_image = [sg.Image('', key='-QRCODE-')]

layout = [
    [sg.Text('input a text to generate qr code', text_color='black', background_color='yellow')],
    [sg.Input('', key='-TEXT-')],
    [sg.Button('create', key='-CREATE-', button_color=('white', 'green'))],
    [sg.Column([qr_image], justification='center')]

]

window = sg.Window(" QR CODE GENERATOR", layout, background_color='yellow')

while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event == '-CREATE-':
        text = values['-TEXT-']
        if text:
            img = qrcode.make(text)
            img.save('qr_code.png')
            window['-QRCODE-'].update('qr_code.png')

window.close()