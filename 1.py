
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('res/genji.jpg')
#if img==None:
if img is None:
    raise RuntimeException("cannot open target image file")
    
b, g, r = cv2.split(img)
#img = cv2.merge((b,g,r))
img[:,:,2] = 0
    
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    #cv2.imwrite('eye_copy.png', img)
    cv2.imwrite('eye_copy.png', img)
    cv2.destroyAllWindows()
