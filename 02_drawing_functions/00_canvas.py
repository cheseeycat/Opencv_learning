import cv2
import numpy as np
import matplotlib.pyplot as plt 

canvas = np.zeros((512,512,3), dtype=np.uint8) + 100
# print(canvas) 
cv2.imshow("canvas", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()
