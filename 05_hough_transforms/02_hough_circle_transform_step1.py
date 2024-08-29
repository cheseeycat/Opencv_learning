import cv2
import numpy as np

img1 = cv2.imread("C:/Users/Melih/Downloads/coins.jpg")
img2 = cv2.imread("C:/Users/Melih/Downloads/balls.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1_blur = cv2.medianBlur(gray1,5)
img2_blur = cv2.medianBlur(gray2,5)

circles1 = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img1.shape[0]/5, param1=200, param2=10,minRadius=70,maxRadius=75)
circles2 = cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT, 1, img2.shape[0]/5, param1=200, param2=10,minRadius=70,maxRadius=75)

if circles1 is not None:
    circles = np.uint16(np.around(circles1))
    for i in circles[0,:]:
        cv2.circle(img1, (i[0],i[1]), i[2], (0,255,0), 2)
        cv2.circle(img1, (i[0],i[1]), 2, (0,0,255), 3)
        
cv2.imshow("coins", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
