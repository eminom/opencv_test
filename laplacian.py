

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('res/genji.jpg')#, cv2.IMREAD_UNCHANGED)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

def rm():
    plt.xticks([])
    plt.yticks([])

laplacian = 1 - laplacian
cv2.imshow('image', laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
plt.subplot(221), plt.imshow(img, cmap='gray')
rm()
plt.subplot(222), plt.imshow(laplacian, cmap='gray')
rm()
plt.subplot(223), plt.imshow(sobelx, cmap='gray')
rm()
plt.subplot(224), plt.imshow(sobely, cmap='gray')
rm()
plt.show()
"""
