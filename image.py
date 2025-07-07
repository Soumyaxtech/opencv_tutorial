import cv2

# to know about shape of an image ...................

image = cv2.imread(r'C:\Users\Soumyajit Koley\Downloads\OIP.jpeg')

print(image.shape) # provide height , width , number of channels  o/p--->(220,331,3)

# to know about type of the image ...................

print(type(image))  # o/p---> <class 'numpy.ndarray'>