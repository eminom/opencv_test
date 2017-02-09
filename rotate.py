

import numpy as np
import cv2

img = cv2.imread('res/genji.jpg', 0)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imwrite('outs/g_rotated.jpg', dst)
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()