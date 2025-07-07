import cv2

import os

# how to read images.......... req import os and imread()

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP.jpeg')
image = cv2.imread(image_path)

# how to write images........... req imwrite()

cv2.imwrite(os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'OIP01.jpeg'),image)

# how to visualized image ......... req imshow()

cv2.imshow('lion',image)
cv2.waitKey(0)  # it is mandetory, it is in milisecond 

#  to visualized image we have to 1st read the image we can't provide
#  write image path here as imwrite() save the image but returns true or false not image
# so to visualized written image we have read it again