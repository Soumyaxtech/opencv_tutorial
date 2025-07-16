import cv2

import os

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'handwriting.jpg')
image = cv2.imread(image_path)

resized_img = cv2.resize(image,(500,570))

gray_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(gray_img,100,255,cv2.THRESH_BINARY)

#  .. two types of adaptive thresholding .........................

thresh = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)

thresh2 = cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,30)

cv2.imshow('frame',resized_img)
cv2.imshow('frame1',gray_img)
cv2.imshow('frame2',thresh1)
cv2.imshow('frame3',thresh)
cv2.imshow('frame4',thresh2)
cv2.waitKey(0)