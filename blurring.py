import os

import cv2

# blurring an image ............................

image = cv2.imread(os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP.jpeg'))

#### method 1 --> CLASSICAL BLURRING ...................

ksize = 5
blur_img = cv2.blur(image, (ksize,ksize))
blur_img1 = cv2.blur(image, (10,5))

cv2.imshow('frame',image)
cv2.imshow('frame1',blur_img)
cv2.imshow('frame2',blur_img1)

#### method 2 ---> GAUSSIAN BLURRING ......................

gaus_blur_img = cv2.GaussianBlur(image,(ksize,ksize),10,5)

cv2.imshow('frame3',gaus_blur_img)

#### method 3 ---> MEDIAN BLURRING .....................

mid_img = cv2.medianBlur(image,ksize)

cv2.imshow('frame4',mid_img)
cv2.waitKey(0)

cv2.destroyAllWindows()