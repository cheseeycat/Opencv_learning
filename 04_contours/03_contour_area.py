import cv2
import numpy as np

img = cv2.imread('C:/Users/Melih/Downloads/contour.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)
M = cv2.moments(cnt)
print(M['m00']) # area of the contour

perimeter = cv2.arcLength(cnt, True)
print(perimeter)

# cv2.imshow('Image', img)
# cv2.imshow('Gray', img_gray)
# cv2.imshow('Thresh', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()