import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((500,500), np.uint8)
b,g,r = cv2.split(img)
cv2.rectangle(img, (20, 60), (250, 200), (255), -1)
cv2.imshow('img', img)
#plt.hist(img.ravel(),256,[0,256]) # ravel() returns a contiguous flattened array
#checkout what means plt.hist() in the documentation
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()