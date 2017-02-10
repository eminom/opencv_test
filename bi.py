

import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy

img = cv2.imread('res/genji.jpg', cv2.IMREAD_UNCHANGED)
dst = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('genji', img)
cv2.waitKey(0)
cv2.imshow('genji', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()





