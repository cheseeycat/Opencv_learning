import cv2
import numpy as np

img = cv2.imread('C:/Users/Melih/Downloads/contour.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # 127 threshold value, 255 max value for pixel
M = cv2.moments(thresh)
X = int(M['m10']/M['m00']) # x coordinate of centroid
Y = int(M['m01']/M['m00']) # y coordinate of centroid
cv2.circle(img, (X, Y), 5, (0, 0, 255), -1) # draw a circle at the centroid
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
                 