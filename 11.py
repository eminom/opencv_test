
import numpy as np
import cv2

e1 = cv2.getTickCount()
img1 = cv2.imread('res/genji.jpg', cv2.IMREAD_UNCHANGED)
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)