import PySimpleGUI as sg      

layout = [[sg.Text('ワンショットウィンドウ')],      
                 [sg.InputText()],      
                 [sg.Submit('送信'), sg.Cancel('X')]]      

window = sg.Window('ウィンドウタイトルバー', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('入力したもの', text_input)