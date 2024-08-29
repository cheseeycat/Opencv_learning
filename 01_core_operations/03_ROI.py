# ROI means Region of interest
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/opencv_udemy/01_core_operations/test_images/orange-parrots-8608540_640.jpg")

roi = img[0:100, 0:100]

cv2.imshow("Original Image", img)
# cv2.imshow("ROI", roi)
cv2.waitKey(3000)
cv2.destroyAllWindows()