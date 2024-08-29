import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/opencv_udemy/01_core_operations/test_images/flamingo-8749724_640.jpg", )

print(img.shape) # (640, 640, 3) - 640x640 resolution, 3 channels (RGB) Reso, Color, Channel
# if channel = 3 -> RGB
# if channel = 1 -> Gray
cv2.imshow("", img) 
cv2.waitKey(3000)

# print("width {} pixels".format(img.shape[1]))
# print("image size {} pixels".format(img.size))
print("data type {}".format(img.dtype))