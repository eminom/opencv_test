

import numpy as np
import cv2

isQuit = False
while not isQuit:
    cap = cv2.VideoCapture('res/match.avi')
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([50, 0, 0])
        upper_blue = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = frame
        #cv2.imshow('frame', frame)
        #cv2.imshow('frame', res)
        cv2.imshow('frame', mask)
        #cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            isQuit = True
            break
    cap.release()
#And then
cv2.destroyAllWindows()
