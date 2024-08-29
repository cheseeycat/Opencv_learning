import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3), dtype=np.uint8) # + x - piyasadaki her pixele x kadar rgb degeri atar
cv2.namedWindow("image")

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
switch = "0 : OFF\n1 : ON"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        img[:] = 0
    if s == 1:
        img[:] = [b, g, r]
    


cv2.destroyAllWindows()