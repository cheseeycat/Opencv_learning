import cv2
import numpy as np
#GRAYSCALE
img = cv2.imread('gradient.png',0)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) #Belirli bir alanı eşiğe tabi tutar ve açık olanları beyaz, kapalı olanları siyah yapar.
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) #Belirli bir alanı eşiğe tabi tutar ve açık olanları beyaz, kapalı olanları siyah yapar.
cv2.imshow('img', img)
cv2.imshow('th1', th1)
