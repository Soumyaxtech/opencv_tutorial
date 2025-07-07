import os

import cv2

webcam = cv2.VideoCapture(0)

while True:
    
    ret,frame= webcam.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xFF == ord('p'):  # it means wait 40 milisec in every frame 
        break                               # when user press p terminate webcam

webcam.release()
cv2.destroyAllWindows()