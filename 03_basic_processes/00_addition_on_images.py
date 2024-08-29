import cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype="uint8") + 255
rectangle = np.zeros((512, 512, 3), dtype="uint8") + 255
cv2.rectangle(rectangle, (150, 150), (450, 450), (255, 0, 0), -1)

cv2.circle(circle, (256, 256), 30, (0, 255, 0), -1)

#cv2.imshow("Circle", circle)
#cv2.imshow("Rectangle", rectangle)
add = cv2.add(circle, rectangle)
cv2.imshow("Addition", add)
cv2.waitKey(0)
cv2.destroyAllWindows()