import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (50, 50), (250, 150)
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100)

cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA) # 3 : thickness

## 사각형 그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4) #pt1 & pt2 : 시작 좌표 / 종료 좌표
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)  #roi : 시작 / 종료 / 너비 / 높이
cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED) # 시작 / 종료 / 너비 / 높이

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
