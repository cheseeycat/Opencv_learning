import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
row,col = img.shape[:2]

M = cv2.getRotationMatrix2D((col/2,row/2),90,1) #parantezi unutmamanız gerekiyor.

dst = cv2.warpAffine(img,M,(col,row)) #90 derece döndürme işlemi yapılır. #col,row değerleri değişir.