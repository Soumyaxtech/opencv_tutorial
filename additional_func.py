import cv2

import os

import numpy as np


image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'opencv_messi.jpg')
image = cv2.imread(image_path)

resized_img = cv2.resize(image,(450,600))


img_edge = cv2.Canny(resized_img,200,300)  # edge detection

dilate_img = cv2.dilate(img_edge,np.ones((2,2),dtype=np.int8))  #dilate edges

erode_img = cv2.erode(img_edge,np.ones((1,1),dtype=np.int8))  #erode edges


#cv2.imshow('frame',resized_img)
cv2.imshow('frame1',img_edge)
cv2.imshow('frame2',dilate_img)
cv2.imshow('frame3',erode_img)
cv2.waitKey(0)