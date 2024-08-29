import cv2
import numpy as np

cap = cv2.VideoCapture("C:/Users/Melih/Downloads/Video/dog.mp4") # open the video

while(1):
    _,frame = cap.read() # Read the frame // LEARN ABOUT HSV
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert the frame to HSV
    
    sensivity = 15 # Define the sensivity
    lower_white = np.array([0,0,255-sensivity], dtype=np.uint8) # Define the lower white threshold
    upper_white = np.array([255,sensivity,255], dtype=np.uint8) # Define the upper white threshold
    
    mask = cv2.inRange(hsv, lower_white, upper_white) # Apply the mask to the frame
    res = cv2.bitwise_and(frame, frame, mask=mask) # Apply the mask to the frame
    cv2.imshow('frame', frame) # Show the frame
    cv2.imshow('mask', mask) # Show the mask
    cv2.imshow('res', res) # Show the result
    
    if cv2.waitKey(5) and 0xFF == ord('q'): # If the user presses 'q' break the loop
        break
cv2.destroyAllWindows() # Close the windows