import cv2

import os

image_path = os.path.join('C:\\Users','Soumyajit Koley','Downloads','birds.jpeg')
image = cv2.imread(image_path)

img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv2.contourArea(cnt))

for cnt in contours:
    if cv2.contourArea(cnt)>1200:
        cv2.drawContours(image,cnt,-1,(0,0,255),1)

        x1,y1,w,h = cv2.boundingRect(cnt)
        
        cv2.rectangle(image,(x1,y1),(x1+w,y1+h),(255,0,0),2)
    
    

cv2.imshow('frame',image)
cv2.imshow('frame1',img_gray)
cv2.imshow('frame2',thresh)
cv2.waitKey(0)