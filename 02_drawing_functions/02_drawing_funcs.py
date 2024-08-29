import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) # + x piyasadaki her pixele x kadar rgb degeri atar
cv2.line(canvas, (25,25), (511,511), (255,0,0), 3) # 25 starting location, 511 ending location, and the 3 is the thickness of the line
cv2.line(canvas, (10,444), (500,400), (0,0,255), 5)# x,y is the listing
cv2.rectangle(canvas, (100,100), (250,250), (0,255,0), 2) # 100,100 is the top left corner, 250,250 is the bottom right corner
cv2.circle(canvas, (400,400), 50, (255,0,255), 3) # 400,400 is the center of the circle, 50 is the radius of the circle and 3 is the thickness of the circle 255,255,255 is the color of the circle
cv2.putText(canvas, "Hello World", (75,290), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 3) # 75,290 is the starting location of the text, 2 is the font size, 3 is the thickness of the text
cv2.ellipse(canvas, (250, 270), (200,60), 0, 0, 360, (0,255,0), 5 ) # 250,270 is the center of the ellipse, 200,60 is the major and minor axis, 00 is the angle of rotation, 0 is the starting angle, 360 is the ending angle, 3 is the thickness of the ellipse
p1 = (100,100)
p2 = (500,200)
p3 = (500,400)

cv2.line(canvas, p1, p2, (255,255,255), 3)
cv2.line(canvas, p2, p3, (255,255,255), 3) #ÜÇGEN
cv2.line(canvas, p3, p1, (255,255,255), 3)  

cv2.polylines(canvas, [np.array([p1,p2,p3])], True, (255,255,255), 3) #POLYLINE

cv2.imshow("Canvas", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()
 