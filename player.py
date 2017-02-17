

import cv2
import numpy as np

target_path = r'f:\Mov\Deadpool.mp4'
isNotQuit = True
while isNotQuit:
    cap = cv2.VideoCapture(target_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            isNotQuit = False
            break
        dest = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dest = cv2.GaussianBlur(dest, (7, 7), 1.5, 1.5)
        dest = cv2.Canny(dest, 0, 30, 3)   # Canny 边缘检测.
        cv2.imshow("Dest", dest)
        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('q') or input_key == 27:
            isNotQuit = False
            break
    cap.release()
cv2.destroyAllWindows()

