import cv2

import os

#img_path = os.path.join('C:\\Users','Soumyajit Koley','OneDrive','Documents','noise.jpg')

image = cv2.imread(r"C:\Users\Soumyajit Koley\OneDrive\Documents\noise.jpg")

ksize = 5

blur_img = cv2.blur(image,(ksize,ksize))

g_blur_img = cv2.GaussianBlur(image,(ksize,ksize),5,3)

m_blur_img = cv2.medianBlur(image,ksize)    # this is best for removing noise

cv2.imshow('frame',image)
cv2.imshow('frame1',blur_img)
cv2.imshow('frame2',g_blur_img)
cv2.imshow('frame3',m_blur_img) 
cv2.waitKey(0)