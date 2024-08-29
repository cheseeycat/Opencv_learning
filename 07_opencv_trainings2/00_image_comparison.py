import cv2
import numpy as np

path = "C:/Users/Melih/Downloads/aircraft.jpg"

img1 = cv2.imread(path)
img1 = cv2.resize(img1,(640,550))
img2 = cv2.imread(path)
img2 = cv2.resize(img2,(640,550))

if img1.shape == img2.shape:
    print("The images have the same size and channels")
    diff = cv2.subtract(img1,img2)
    b,g,r = cv2.split(diff)
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")
    else:
        print("The images are not equal")
        cv2.imshow("img1",img1)
        cv2.imshow("img2",img2)
        cv2.imshow("diff",diff)
        cv2.waitKey(0)
        cv2.destroyAllWindows()









cv2.imshow("img",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
