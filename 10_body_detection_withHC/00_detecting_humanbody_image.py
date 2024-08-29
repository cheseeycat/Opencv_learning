import cv2

img = cv2.imread("C:/opencv_udemy/haar_Cascade/Body.jpg")

body_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/fullbody.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(gray,1.80,1)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()