import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/opencv_udemy/01_core_operations/test_images/orange-parrots-8608540_640.jpg")
# print(img)
corner = img[0:100, 0:100] # y1:y2, x1:x2
img[0:100, 0:600] = [255, 24, 255]

cv2.imshow("imaj", img)

cv2.waitKey(3000)
cv2.destroyAllWindows()