#basic motion detection system
import cv2
cap=cv2.VideoCapture('Cars - 1900.mp4')

# first read 2 frames
ret,frame1=cap.read()
ret,frame2=cap.read()


while(True):
    #finding differece
    diff=cv2.absdiff(frame1,frame2)#this function calculates the absolute difference

    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #to fill the holes where not needed
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        x,y,w,h=cv2.boundingRect(contour) #this gives the height width around a contour
    
    # to filter non necessary motion
        if cv2.contourArea(contour)<15000:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame1,"status: ()".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)



    cv2.imshow('vdo',frame1)
    frame1=frame2
    _,frame2=cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()#to release the camera
cv2.destroyAllWindows()