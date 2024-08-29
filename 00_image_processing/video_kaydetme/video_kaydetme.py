import cv2

cap = cv2.VideoCapture(0)

videoFileOutput = cv2.VideoWriter("C:/opencv_udemy/01_image_processing/video_kaydetme/video.avi", cv2.VideoWriter_fourcc('W', 'M', 'V', '2'), 30.0, (640, 480))    # 20.0 is the frame rate, (640, 480) is the resolution  q
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)
    
    cv2.imshow("Webcam live", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()