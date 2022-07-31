import cv2
from random import randrange

#import haar cascade algorithm pre-trained data

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_data = cv2.CascadeClassifier("haarcascade_smile.xml")


#image to detect the faces

#img = cv2.imread("C:\Users\503266786\Documents\Python-AI\Elon_Musk_Royal_Society_(crop2).JPEG")

# 0-default webcam, or video filename/path
webcam = cv2.VideoCapture(0)

key = cv2.waitkey(1)

#iterate over frames of video
while True:

    # Read the current frame
    read_current_frame, frame = webcam.read()

    if not read_current_frame:
        break
    

    #print(img)
    #this is a list of img cord
    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cord = trained_face_data.detectMultiScale(grey_img, scaleFactor=1.7, minNeighbours=20)
    
    
    #rectangle around the faces

    for (x, y, w, h) in face_cord:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 1)


        # the face ( crop details )
        the_face = frame[x:x+w, y:y+h]
        grey_img = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)
        smile_cord = smile_data.detectMultiScale(grey_img)

        if len(smile_cord)>0:
            for (x_, y_, w_, h_) in smile_cord:
                cv2.rectangle(frame, (x_, y_), (x_+w_, y_+h_), (randrange(128, 255), randrange(128, 255), randrange(128, 255)), 1)
                cv.putText(frame, "smiling", (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color(255,255,255))

     #print(face_cord)
     cv2.imshow('Smile detection app', frame)

     if key == 81 or key ==113:
         break


#releasing/cleanup release
webcam.release()
cv2.destroyAllWindows()

print("code completed")