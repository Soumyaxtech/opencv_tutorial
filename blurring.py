import os

import cv2

# blurring an image ............................

image = cv2.imread(os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP.jpeg'))

#### method 1 --> CLASSICAL BLURRING ...................

blur_img = cv2.blur(image, (5,5))
blur_img1 = cv2.blur(image, (10,5))

cv2.imshow('frame',image)
cv2.imshow('frame1',blur_img)
cv2.imshow('frame2',blur_img1)
cv2.waitKey(0)

cv2.destroyAllWindows()