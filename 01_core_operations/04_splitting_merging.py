import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:/opencv_udemy/01_core_operations/test_images/opencv-icon-1657x2048-3wu3ib6x.png")
(B, G, R) = cv2.split(img)

merged = cv2.merge([B, G, R])

cv2.imshow("Original Image", img)
cv2.imshow("b", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

