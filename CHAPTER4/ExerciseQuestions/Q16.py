import numpy as np
import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")

title = "16"
mask = np.zeros((480, 640), np.uint8)
mask[100:300, 200:300] = 1

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    blue, green, red = cv2.split(frame)
    cv2.add(green, 50, green, mask=mask)
    frame = cv2.merge([blue, green, red])
    cv2.imshow(title, frame)
capture.release()