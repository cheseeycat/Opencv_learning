import cv2
import numpy as np

img = cv2.imread('C:/Users/Melih/Downloads/text.png') # Load an image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

gray = np.float32(gray) # Convert the image to float32
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # Find the corners /// corner,qulityLevel,minDistance
corners = np.int0(corners) # Convert the corners to int0

for i in corners:
    x,y = i.ravel() # ravel() returns a contiguous flattened array
    cv2.circle(img, (x,y), 3, 255, -1) # Draw a circle on the image 


cv2.imshow('corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
