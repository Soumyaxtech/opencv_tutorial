import cv2

import os

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'bear.jpg')
image = cv2.imread(image_path)

#............. SIMPLE OR GLOBAL THRESHOLDING ..........................................

#   1st step ---> convert image to gray scale.............

gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#   then thresholding on the grayscale image.................

ret,thresh = cv2.threshold(gray_img,100,255,cv2.THRESH_BINARY)

# cv2.threshold() returns two values ret and thresh ret---> threshold value    and             thresh----> o/p binary image 

# now if we want to remove noises that present on the binary image we use blur then again threshold we get smooth binary image.....................

blur_img = cv2.blur(thresh,(7,7))

ret,thresh1 = cv2.threshold(blur_img,100,255,cv2.THRESH_BINARY)

print(ret)  # return thresholding value o/p ---> 100.0
cv2.imshow('frame',image)
cv2.imshow('frame1',gray_img)
cv2.imshow('frame2',thresh)
cv2.imshow('frame3',thresh1)
cv2.waitKey(0)