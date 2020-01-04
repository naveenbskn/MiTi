###########################################################################################
#created by    : Naveen
#last modified :31/12/19
############################################################################################

import PySimpleGUI as sg
import qrcode
import os
import img_view
import shutil
def g():
    event, values = sg.Window('Tina', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
    if((values[0])==None):
        pass
    else:

        
        a=(values[0])
        try:
            shutil.copy(a, r'C:\xampp\htdocs\tina')
            r=str(a)
            b=(r.split('/'))
            s=b[-1]
            #print(b)
            t='http://192.168.43.142/tina/'+s
            img = qrcode.make(t)
            img.save('test.png')
            try:
                exec(img_view.i())
            except:
                a=1
        except:
                a=1
