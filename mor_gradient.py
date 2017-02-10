

import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8)

img = cv2.imread('res/save_uno.png', cv2.IMREAD_UNCHANGED)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

for img in [img, gradient]:
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

