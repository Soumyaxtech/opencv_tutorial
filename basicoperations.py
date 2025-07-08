import os

import cv2 

# resizeing image ..............................


image_path = os.path.join('C:\\Users', 'Soumyajit Koley','OneDrive', 'Documents', 'nature.jpg')

image = cv2.imread(image_path)

resized_img = cv2.resize(image,(1300,600)) # here --->width,height but imshow()---> height,width


print(image.shape)
print(resized_img.shape)

cv2.imshow('original',image)
cv2.imshow('resized',resized_img)



# cropping image...........................

img = cv2.imread(os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP.jpeg'))

cropped_img = img[25:180,75:245]

print(img.shape)
print(cropped_img.shape)
cv2.imshow('lion',img)
cv2.imshow('croplion',cropped_img)
cv2.waitKey(0)