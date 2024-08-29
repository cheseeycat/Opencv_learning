import cv2

cap = cv2.VideoCapture(0)
circle = []
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circle.append((x, y))
cv2.namedWindow("Frame")

cv2.setMouseCallback("Frame", mouse_event)

while 1:
    ret, frame = cap.read()
    for center in circle:
        cv2.circle(frame, center, 20, (0, 255, 0), -1)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey == ord('w'):
        circle = []
cap.release()
cv2.destroyAllWindows()