import PySimpleGUI as sg      

layout = [[sg.Text('ワンショットウィンドウ')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('ウィンドウタイトルバー', layout)    

event, values = window.read()    
window.close()

text_input = values['-IN-']    
sg.popup('You entered', text_input)