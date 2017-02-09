
import numpy as np
import cv2

img = cv2.imread('res/eye.png', 0)
# 这时候是一张灰度图
# (src, ksize, sigmaX)
blur = cv2.GaussianBlur(img, (5, 5), 0)
# (images, channels, mask, histSize, ranges)
hist = cv2.calcHist([blur], [0], None, [256], [0,256])

#if True:
    # Do some test
    #a = hist.ravel()
    #print(a)
    #for i in range(len(a)-1):
    #    assert a[i] <= a[i+1], "Error seq for {0}".format(i)

# 分布.
# hist_dist = hist.ravel() / hist.sum() #这才是概率分布函数.

hist_norm = hist.ravel() / hist.max()
# 归一化; 如同hist.T / hist.max().  最大的那根柱子是1.

Q = hist_norm.cumsum()   #累积和.
bins = np.arange(256)
fn_min = np.inf
thresh = False

# 一样的尺码.
assert hist_norm.shape == bins.shape
# Q[-1] is sum(hist_norm)
# 找到让方差最小的threshold的值.
for i in range(1, 256):
    #用index进行切割.(0或者超过都是可以的)
    p1, p2 = np.hsplit(hist_norm, [i])
    q1, q2 = Q[i], Q[-1] - Q[i]
    b1, b2 = np.hsplit(bins, [i])
    m1 = 0 if 0 == q1 else np.sum(p1 * b1) / q1
    m2 = 0 if 0 == q2 else np.sum(p2 * b2) / q2
    v1 = 0 if 0 == q1 else np.sum((b1-m1)**2*p1) / q1
    v2 = 0 if 0 == q2 else np.sum(((b2-m2)**2)*p2) / q2
    v1 = v1 if q1 != 0 else 0
    v2 = v2 if q2 != 0 else 0
    fn = v1 * q1 + v2 * q2
    #print("fn is {0}".format(fn))
    if not thresh or fn < fn_min:
        fn_min = fn
        thresh = i
#print("fn_min is {0}".format(fn_min))
# 和系统的cv2.THRESH_OTSU(实现)做比较.
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(thresh, ret)

