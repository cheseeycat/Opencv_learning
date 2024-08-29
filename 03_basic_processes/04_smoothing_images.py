import cv2
import numpy as np

img_filter = cv2.imread('images/lena.jpg')
img_median = cv2.imread('images/lena.jpg')
img_bilateral = cv2.imread('images/lena.jpg')

blur = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
blur_g = cv2.blur(img_filter, (5, 5))
blur_m = cv2.medianBlur(img_median, 5)
blur_b = cv2.bilateralFilter(img_bilateral, 9, 95, 75) # pütürleri azaltır

cv2.imshow('Median', blur_m)
cv2.imshow('Blur', blur)
cv2.imshow('Original', img_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()
