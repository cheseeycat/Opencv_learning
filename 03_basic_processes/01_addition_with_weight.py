import cv2
import numpy as np
# f(x,y) = x*a + y*b + c
circle = np.zeros((512, 512, 3), dtype="uint8") + 255
rectangle = np.zeros((512, 512, 3), dtype="uint8") + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (255, 0, 0), -1)
cv2.circle(circle, (256, 256), 100, (0, 255, 0), -1)

dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)

cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()