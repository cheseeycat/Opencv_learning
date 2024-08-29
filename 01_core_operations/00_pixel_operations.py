import cv2
import numpy as np

img = cv2.imread("C:/Coding/opencv_udemyy/01_core_operations/test_images/opencv-icon-1657x2048-3wu3ib6x.png")
for i in range(550, 560):
    for j in range(380, 390):    
        px = img[i,j]
        print(px)

# (b, g, r) = img[50, 30]
# print("50,30 - red: {}, green: {}, blue: {}".format(r, g, b))

# b = 0
# g = 2
# r = 1

#accessing only one channel
blue = img[100, 100, 0]
red = img[100, 100, 1]
green = img[100, 100, 2]

print("before", img[100, 100])
img[100, 100] = [100, 100, 100] 
print("after", img[100, 100])
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# img.item(100,100,2) (B, G, R - 0, 1, 2)
# img.item((100,100,2), 100) (B, G, R - 0, 1, 2) convert that pixel value to 100

