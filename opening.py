
import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
img = cv2.imread('res/i_with_noisy.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('destionation', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()

