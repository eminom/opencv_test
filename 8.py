
import numpy as np
import cv2
from matplotlib import pyplot as plt

# IMREAD_ANYDEPTH
# IMREAD_COLOR
img = cv2.imread('res/genji.jpg', cv2.IMREAD_UNCHANGED)
#plt.imshow(img, cmap='gray', interpolation='bicubic')
img += img
plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.xticks([]), plt.yticks([])
plt.show()