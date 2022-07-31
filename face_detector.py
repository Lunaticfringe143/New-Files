import cv2
from random import randrange

#import haar cascade algorithm pre-trained data

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


#image to detect the faces

#img = cv2.imread("C:\Users\503266786\Documents\Python-AI\Elon_Musk_Royal_Society_(crop2).JPEG")

# 0-default webcam, or video filename/path
webcam = cv2.VideoCapture(0)

#iterate over frames of video
while True:

    # Read the current frame
    read_current_frame, frame = webcam.read()

    key = cv2.waitkey(1)

    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #print(img)
    #this is a list of img cord
    face_cord = trained_face_data.detectMultiScale(grey_img)
    
    #rectangle around the faces

    for (x, y, w, h) in face_cord:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 1)



     

     #print(face_cord)
     cv2.imshow('face detection app', frame)

     if key == 81 or key ==113:
         break

webcam.release()

print("code completed")