
import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
img = cv2.imread('res/i.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('image', img)
cv2.waitKey(0)

for i in range(1,4):
    dst = cv2.dilate(img, kernel, iterations = i)
    cv2.imshow('image', dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()

