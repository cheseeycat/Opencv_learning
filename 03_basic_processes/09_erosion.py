import cv2 
import numpy as np

img = cv2.imread('messi5.png',0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel,iterations = 1) #erosion followed by dilation, removes noise
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel,iterations = 1) #dilation followed by erosion, fills holes
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel,iterations = 1) #difference between dilation and erosion of an image
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel,iterations = 1) #difference between input image and opening of the image, destroys intersection points
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel,iterations = 1) #difference between the closing of the input image and input image, destroys non-intersection points

#
#
cv2.imshow('closing', closing)
cv2.imshow('opening', opening)
cv2.imshow('img', img)
