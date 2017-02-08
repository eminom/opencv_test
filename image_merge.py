
import numpy as np
import cv2


def add_print(src_bg, fg_img, offset):
    SHOW = False
    mode = cv2.IMREAD_UNCHANGED
    src_bg = cv2.imread(src_bg, mode)
    print("shape of bg is:{0}".format(src_bg.shape))
    fg_img = cv2.imread(fg_img, mode)
    print("shape of role_img is:{0}".format(fg_img.shape))
    # Preprocessing of png image.(the transparent part must be erased)
    alpha_layer = fg_img[:, :, 3]     #Or rather: alpha_layer = fg_img[:,:,3] / 255
    alpha_layer = alpha_layer / 255   #Cannot do `/=' while being of the same type(uint8)
    for i in range(3):
        fg_img[:, :, i] = fg_img[:, :, i] * alpha_layer
    fg_img = fg_img[:, :, :-1]  #And remove the alpha layer for good.

    rows, cols, channels = fg_img.shape
    print(rows, cols, channels)
    x, y = offset
    #roi = src_bg[y:(rows + y), x:(cols+x)]
    roi = src_bg[y:rows+y, x:cols+x]
    print(rows, cols)
    print("shape of roi is:{0}".format(roi.shape))
    img2gray = cv2.cvtColor(fg_img, cv2.COLOR_BGR2GRAY)
    print("shape of gray image is:{0}".format(img2gray.shape))
    #Este es solo de dos dimensioned.
    #
    if SHOW:
        cv2.imshow('gray', img2gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    maxVal = 255
    thresholdVal = 77
    ret, mask = cv2.threshold(img2gray, thresholdVal, maxVal, cv2.THRESH_BINARY)
    assert ret, "Must be true"
    #print("shape of mask is:{0}".format(mask.shape))
    mask_inv = cv2.bitwise_not(mask)
    #img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
    img1_bg = roi
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(fg_img, fg_img, mask = mask)
    #print("shape of img1_bg is:{0}".format(img1_bg.shape))
    #print("shape of img2_fg is:{0}".format(img2_fg.shape))
    dst = cv2.add(img1_bg, img2_fg)
    #dst = img2_fg
    #dst = img1_bg  #This image is not pure. (With role's print on)
    #dst = img1_bg + img2_fg
    bg_img = src_bg
    #bg_img[y:rows+y, x:cols+x] = dst
    bg_img[y:rows+y, x:cols+x] = dst
    cv2.imwrite('hola.jpg', bg_img)

    if SHOW or True:
        cv2.imshow('res', bg_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

add_print('res/genji.jpg', 'res/eye.png', (50, 100))