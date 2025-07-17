import cv2

import os

import cv2.text

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'whiteboard.jpeg')
image = cv2.imread(image_path)

#   how to draw line ......................................

cv2.line(image,(50,30),(100,30),(255,0,0),1)

# in line (1st image --> 1st point coordinate --> 2nd point coordinate --> color --> thickness)

#   how to draw rectangle ..................................

cv2.rectangle(image,(50,50),(100,100),(0,255,0),3)  # upper co , lower co , color , thickness

#   how to draw circle ...................................

cv2.circle(image,(150,70),30,(0,0,255),3)   # center , radius , color , thickness




cv2.imshow('frame',image)
cv2.waitKey(0)