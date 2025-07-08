import os

import cv2

img = cv2.imread(os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP.jpeg'))

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_hsv1 = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2HSV)
cv2.imshow('frame',img)
cv2.imshow('frame1',img_rgb)
cv2.imshow('frame2',img_gray)
cv2.imshow('frame3',img_hsv)
cv2.imshow('frame4',img_hsv1)
cv2.waitKey(0)