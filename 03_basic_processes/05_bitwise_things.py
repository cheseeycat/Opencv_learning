import numpy as np
import cv2
img1 = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
# Siyahlar 1 Beyazlar 0 ve matematiksel mantık işlemleri uygulanır.
cv2.bitwise_and(img1, img2) #img1 and img2 gets compared bitwise
bit_and = cv2.bitwise_and(img1, img2) #img1 and img2 gets compared bitwise and stored in bit_and
bit_or = cv2.bitwise_or(img1, img2) #img1 and img2 gets compared bitwise or stored in bit_or
bit_xor = cv2.bitwise_xor(img1, img2) #img1 and img2 gets compared bitwise xor stored in bit_xor
bit_not1 = cv2.bitwise_not(img1) #img1^-1 bitwise not stored in bit_not1
bit_not2 = cv2.bitwise_not(img2) #img2^-1 bitwise not stored in bit_not2

cv2.imshow('bit_and', bit_and)
cv2.waitKey(0)
cv2.destroyAllWindows()