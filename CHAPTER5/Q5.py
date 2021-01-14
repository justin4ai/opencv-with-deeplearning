import numpy as np, cv2

image = np.zeros((300, 400), np.uint8)
image[:] = 100

title = 'Window'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.moveWindow(title, 100, 200)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 'Window' 라는 이름의 윈도우가 생기며, 좌측 최상단 기준 X축 -> 100, Y축 -> 200 만틈 이동
## 색깔은 100(회색)이다.
## 사이즈는 100 x 200 행렬 꼴이며, WINDOW_NORMAL을 사용했기 때문에 사이즈는 가변이다.

import numpy as np, cv2

image = np.zeros((400, 600, 3), np.uint8)
image[:] = (255, 255, 255)
pt1, pt2 = (50, 100), (200, 300)

cv2.line(image, pt1, pt2, (0,255,0), 5)
cv2.rectangle(image, pt2, (300, 400), (0, 0, 255), -1, cv2.LINE_4, 1)

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 윈도우의 배경은 흰색 (255, 255, 255)이다.
## 배경 사이즈는 400 x 600 행렬이고, 채널은 3 채널이다.
## image라는 윈도우에 pt1부터 pt2를 잇는 초록색 (cv2는 B, G, R순이기 때문에) 선을 굵기 5로 그린다.
## image라는 윈도우에 pt2와 (300, 400)를 대각 꼭짓점으로 하는 사각형을 굵기 1의 빨간색 4방향 선으로 그린다.