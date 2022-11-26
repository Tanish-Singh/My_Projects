#lane detetction on a video
import cv2
import numpy as np

#region or interest function, rest will be masked
def region_of_interest(img,roi):
    mask=np.zeros_like(img)
    match_mask_color=255
    cv2.fillPoly(mask,roi,match_mask_color)
    mask_image=cv2.bitwise_and(img,mask)
    return mask_image

#draw the lines function
def draw_lines(img, lines):
    img=np.copy(img)
    img_cpy=np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img_cpy,(x1,y1),(x2,y2),(0,255,0),3)
    
    imgx=cv2.addWeighted(img,0.8,img_cpy,1,0.0)
    return imgx

def process(image):
    height=image.shape[0]
    width=image.shape[1]
    region_of_interest_vertices=[(0,height),(0,width/6),(width,height/8),(width*0.9,height),(0,height)]
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(gray,100,200)
    cropped_image=region_of_interest(canny,np.array([region_of_interest_vertices],np.int32))
    #hoough line after getting the cropper image 
    lines=cv2.HoughLinesP(cropped_image,6,np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=70)

    #calling the draw line function
    image_lines=draw_lines(image,lines)
    return image_lines

#calling all the functions
cap=cv2.VideoCapture('Road - 80397.mp4')
while(cap.isOpened()):
    _,frame=cap.read()
    frame=process(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cap.destroyAllWindows()