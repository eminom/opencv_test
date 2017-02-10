

import cv2
import numpy as np

# 参数取自Player.cpp
def show_target(file):
    img = cv2.imread('res/{0}'.format(file), cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.GaussianBlur(img, (5,5), 1.5, 1.5)
    dst = cv2.Canny(dst, 0, 30, 3)
    cv2.imshow('destination', dst)
    cv2.waitKey(0)   #Blocking. Otherwise nonblocking

for path in ['B1.jpg']:
    #, 'dorothy_a.png', 'dorothy_b.png', 'dorothy_c.png', 'dorothy_d.png']:
    show_target(path)

cv2.destroyAllWindows()





