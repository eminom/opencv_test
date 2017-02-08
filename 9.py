

import numpy as np
import cv2

bird = cv2.imread('res/bird.png', cv2.IMREAD_UNCHANGED)
eye = cv2.imread('res/eye.png', cv2.IMREAD_UNCHANGED)

dst = cv2.addWeighted(eye, 0.7, bird, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
