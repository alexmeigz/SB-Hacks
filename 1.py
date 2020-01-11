import cv2
import numpy as np

image = cv2.imread("capture.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 20, 40)

kernel = np.ones((3, 3), np.unit8)
dilated = cv2.dilate(canny, kernel, iterations=2)


(contours, hierarchy) = cv2.findContours(dilated.copy(), 
                                         cv2.RETR_TREE,
                                         cv2.CHAIN_APPROX_SIMPLE)
