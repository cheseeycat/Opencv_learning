import cv2
                          # Canny edge detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986. It is a multi-step algorithm that involves the following steps:
cap = cv2.VideoCapture(0) # Open the camera

while 1:
    ret,frame = cap.read() # Read the frame
    frame = cv2.flip(frame, 1) # Flip the frame
    
    edges = cv2.Canny(frame, 100, 200) # Apply the Canny edge detection frmae is frame and 100,200 are the threshold values
    cv2.imshow('edges', edges) # Show the edges
    cv2.imshow('frame', frame) # Show the frame 

    if cv2.waitKey(1) & 0xFF == ord('q'): # If the user presses 'q' break the loop
        break
    
cap.release() # Release the camera
cv2.destroyAllWindows