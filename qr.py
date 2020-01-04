###########################################################################################
#created by    : Naveen
#last modified :3/1/20
############################################################################################

import qrcode
import os
import img_view
def view(r):
    r=str(r)
    t='http://192.168.43.142/tina/'+r
    img = qrcode.make(r)
    img.save('test.png')
    try:
        exec(img_view.i())
    except:
        a=1
