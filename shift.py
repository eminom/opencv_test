

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('res/genji.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
#dst = img
dst = cv2.warpAffine(img, M, (cols, rows))
#plt.imshow(dst)
#plt.show()
print("shape of dst is {0}".format(dst.shape))
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
