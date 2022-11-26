#detect eyes in video
import cv2
facecascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap=cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(gray,2,5)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imshow('frame',frame)
cap.release()