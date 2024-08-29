import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

row,col = img.shape[:2]

m = np.float32([1,0,10],[0,1,70])

dst = cv2.warpAffine(img,m,(col,row))

cv2.imshow('dst',dst)
#resim dışındaki siyah alanları yaratıyor.

