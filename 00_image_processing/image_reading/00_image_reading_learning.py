import cv2

img = cv2.imread("C:/opencv_udemy/01_image_processing/klon.jpg")
# print(img)
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img)
# cv2.imwrite("klon_copy.jpg", img)
cv2.resizeWindow("Image", 1200, 600)
cv2.waitKey(3000)
cv2.destroyAllWindows()