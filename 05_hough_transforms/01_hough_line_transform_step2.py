import cv2
import numpy as np

vid = cv2.VideoCapture("C:/Users/Melih/Downloads/Video/line.mp4")


while 1:
    ret, frame = vid.read()
    cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # // hsv range for yellow color in opencv // is 18-48
    lower_yellow = np.array([18, 94, 140],np.uint8)
    upper_yellow = np.array([48, 255, 255],np.uint8)    
    
    mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
    edges = cv2.Canny(mask, 75, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    
    for i in lines:
        x1,y1,x2,y2 = i[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
        
        
    cv2.imshow("maskedsaw", frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    
    
vid.release()
cv2.destroyAllWindows()