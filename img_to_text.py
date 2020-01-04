###########################################################################################
#created by    : Naveen
#last modified :3/1/20
############################################################################################

import pytesseract #pip install tesseract
import os
from PIL import Image
import cv2

global img_name
def imtopic():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Path to the tesseract 
    src=img_name
    img = Image.open(src)# add Image name here with file extention
    text = pytesseract.image_to_string(img)
    print(text)
    remember = open('remember.txt','w')
    remember.write(text)
    remember.close()
def ta():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Tina")

    img_counter = 0
    try:
        while True:
            ret, frame = cam.read()
            cv2.imshow("Tina", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k%256 == 27:
                # ESC pressed
               
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "img_to_text_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
             
                
                
                img_counter += 1
                imtopic()
        cam.release()
        cv2.destroyAllWindows()
    except:
        c=bin(1)


