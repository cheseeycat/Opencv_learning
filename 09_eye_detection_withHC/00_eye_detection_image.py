import cv2

img = cv2.imread("C:/opencv_udemy/test_images/face.png")
eye_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/eye.xml")
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/frontalface.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.40,6)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    
img2 = img[y:y+h,x:x+w]

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray2,1.40,4)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()