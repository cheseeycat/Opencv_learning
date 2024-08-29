import cv2
import numpy as np

img = cv2.imread("C:/Users/Melih/Downloads/starwars.jpg")

blurry_img = cv2.medianBlur(img,7)

laplacian = cv2.Laplacian(blurry_img,cv2.CV_64F).var()

print(laplacian)

if laplacian < 400:
    print("Image is blurry")

cv2.imshow("Blurred Image",blurry_img)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
