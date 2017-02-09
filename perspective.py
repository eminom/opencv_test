

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('res/eye.png', cv2.IMREAD_UNCHANGED)
rows, cols, _ = img.shape

pts1 = np.float32([[56, 65], [868, 52], [28, 887], [889, 890]])
pts2 = np.float32([[0, 0], [900, 0], [0, 900], [900, 900]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (900, 900))

plt.subplot(121)
plt.imshow(img)
plt.title('original')

plt.subplot(122)
plt.imshow(dst)
plt.title('perspective')
plt.show()
