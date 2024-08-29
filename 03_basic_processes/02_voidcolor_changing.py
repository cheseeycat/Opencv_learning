import cv2

cap = cv2.VideoCapture("C:/Users/Melih/Desktop/melyh.mkv")

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()