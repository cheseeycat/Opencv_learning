import cv2
import numpy as np
import requests

url = ("http://192.168.1.104:8080//shot.jpg") # /shot.jpg is the path of the image from the camera

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)    # Convert the image to a numpy array
    img = cv2.imdecode(img_arr, -1)    # Decode the numpy array to an image cv2.IMREAD_COLOR also works
    img = cv2.resize(img, (640, 480))
    
    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()