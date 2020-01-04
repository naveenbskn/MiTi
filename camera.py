###########################################################################################
#created by    : Naveen
#last modified :31/12/19
############################################################################################
import cv2
def cam():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Tina")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        frame=cv2.flip(frame,1)
        cv2.imshow("Tina", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "Tina_snap_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

