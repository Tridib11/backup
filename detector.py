#Import opencv
import cv2

#Import uuid name images uniquely
import uuid

#Import operating system
import os

#import time
import time
labels=['thumbsup','thumbsdown','thankyou','livelong']  #list
number_img=5  #how many images we are going to collect per class
IMAGES_PATH=os.path.join('Tenserflow','workspace','images','collectedimages')
"""The exclamation mark "!" is used in Jupyter notebooks to indicate
that the following command is a shell command, rather than a Python command"""
if not os.path.exists(IMAGES_PATH):
    if os.name=='posix':  #for linux
        os.mkdir(IMAGES_PATH)
    if os.name=='nt':  #for windows to check write os.name
        os.mkdir(IMAGES_PATH)
for label in labels:
    path=os.path.join(IMAGES_PATH,label)
    if not os.path.exists(path):
        os.mkdir(IMAGES_PATH)
for label in labels:
    cap=cv2.VideoCapture(0) #connects to our webcam
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_img):
        print("Colleting image {}".format(imgnum))
        ret,frame=cap.read()  #capture the frame of our webcam
        imgname=os.path.join(IMAGES_PATH,label,label+"."+"{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(imgname,frame)
        cv2.imshow("frame",frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
cap.release()
cv2.destroyAllWindows()