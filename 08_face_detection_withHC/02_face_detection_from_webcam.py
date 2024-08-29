import cv2
vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/frontalface.xml")

while 1:
    ret,frame = vid.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.40,1)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()