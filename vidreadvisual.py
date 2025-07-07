import os

import cv2

# reading of video.................req videocapture()

video_path = os.path.join('C:\\Users','Soumyajit Koley','Downloads','video for opencv.mp4')

video1 = cv2.VideoCapture(video_path)

# visualizing the video ..............

ret = True

while ret:
    ret, frame = video1.read()  # see notes
   
    if ret: 
        frame = cv2.resize(frame, (800, 600))
        cv2.imshow('video',frame)
        cv2.waitKey(40)
        
video1.release()
cv2.destroyAllWindows()