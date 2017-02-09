


import cv2
import numpy as numpy
from matplotlib import pyplot as plt


if False:
    # Method Uno: Read the gray image.
    img = cv2.imread('res/genji.jpg', 0)
else:
    # Or rather:
    img = cv2.imread('res/genji.jpg', cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#print(img.shape)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C
    , cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    , cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
    'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

for i in range(4):
    # 22: 1,2,3,4
    plt.subplot(2 * 100 + 2 * 10 + i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    #Remove the numeros along the axes
    plt.xticks([])
    plt.yticks([])
plt.show()