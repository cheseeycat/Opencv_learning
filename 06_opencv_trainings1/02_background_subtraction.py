import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Melih/Downloads/Video/car.mp4")
_,first_frame = cap.read()
first_frame = cv2.resize(first_frame, (640, 480))
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5,5), 0) #GaussianBlur is used to reduce noise in the image // softens it
while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(first_gray, (5,5), 0) #GaussianBlur is used to reduce noise in the image // softens it
    
    
    difference = cv2.absdiff(first_gray, gray)
    threshold = cv2.threshold(difference, 5, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("frame",frame)
    cv2.imshow("fframe",first_frame)
    cv2.imshow("dif", difference)
    
    
    # SOMETHING IS WRONG WITH THE CODE CHECK IT OUT LATER
    
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()