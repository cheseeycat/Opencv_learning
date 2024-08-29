import cv2
img = cv2.imread('C:/Users/Melih/Downloads/contour1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

_,thresh = cv2.threshold(gray, 127, 255, 0) # Apply a threshold to the image
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Find the contours in the image // cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE are the retrieval mode and the approximation method respectively
## print(contours) # Print the contours value
cv2.drawContours(img, contours, -1, (0,255,0), 3) # Draw the contours on the image // -1 means draw all the contours, (0,255,0) is the color of the contours, 3 is the thickness of the contours
cv2.imshow("image",img) #show the contoured image
cv2.waitKey(0) # Wait for the user to press a key
cv2.destroyAllWindows() # Close the window