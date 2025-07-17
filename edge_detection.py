import cv2

import os

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'opencv_messi.jpg')
image = cv2.imread(image_path)

resized_img = cv2.resize(image,(450,600))


img_edge = cv2.Canny(resized_img,150,220)   # this values are by trail and error
#print (image.shape)
cv2.imshow('frame',resized_img)
cv2.imshow('frame1',img_edge)
cv2.waitKey(0)