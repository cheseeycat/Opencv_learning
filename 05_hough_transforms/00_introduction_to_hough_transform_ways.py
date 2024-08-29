import cv2
import numpy as np

img = cv2.imread("C:/Users/Melih/Downloads/h_line.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150, apertureSize=3)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200, minLineLength=100)

for i in lines: # Dört tane tuttukları değer noktanın resim üzerindeki analitik koordinatları.
    x1, y1, x2, y2 = i[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)




cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows