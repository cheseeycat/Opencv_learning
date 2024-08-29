import cv2

vid = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/frontalface.xml")
eye_cascade = cv2.CascadeClassifier("C:/opencv_udemy/haar_Cascade/eye.xml")

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.20,10)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.20,3)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
vid.release()
cv2.destroyAllWindows()