###########################################################################################
#created by    : Naveen
#last modified :3/1/20
############################################################################################
from googletrans import Translator
def trans(i):
    a=Translator()
    b=a.translate(i)
    aw=str(b)
    aw=aw.split(",")
    aw=aw[2]
    b=aw[6:]
    #print(aw)


    return(b)

