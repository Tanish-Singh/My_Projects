import tensorflow as tf
import pandas as pd
import numpy as np
import cv2

cnn=tf.keras.models.load_model('/Users/tanishsingh/Downloads/mymodel-2.h5')

cascade=cv2.CascadeClassifier('/Users/tanishsingh/Downloads/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while(cap.isOpened()):
    _,frame=cap.read()
    faces=cascade.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=4)

    #filter the image and drawing Rectangle
    for x,y,w,h in faces:
        face=frame[y:y+h,x:x+w]
        cv2.imwrite('temp.jpg',face)
        face=tf.keras.preprocessing.image.load_img('temp.jpg',target_size=(150,150))
        face=tf.keras.preprocessing.image.img_to_array(face)
        face=np.expand_dims(face,axis=0)
        
        ans=cnn.predict(face)
        
        #condition for mask 
        if ans<0.5:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(frame,'with mask',(x//2,y//2),cv2.FONT_HERSHEY_SIMPLEX,3,(0,255,0),2)
            # thickness
            print('with mask')
        else:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            cv2.putText(frame,'without mask',(x//2,y//2),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2)
            print('without mask')
        
        
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

