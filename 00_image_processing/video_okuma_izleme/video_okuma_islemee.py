import cv2
import numpy as np

# cap = cv2.VideoCapture(0) webcam
cap = cv2.VideoCapture(video linki) # video linki

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    
cap.release()
cv2.destroyAllWindows()