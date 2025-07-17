import cv2

import os

image_path = os.path.join('C:\\Users', 'Soumyajit Koley', 'Downloads', 'whiteboard.jpeg')
image = cv2.imread(image_path)

#   how to draw line ......................................

cv2.line(image,(100,80),(200,80),(255,0,0),1)

# in line (1st image --> 1st point coordinate --> 2nd point coordinate --> color --> thickness)


cv2.imshow('frame',image)
cv2.waitKey(0)