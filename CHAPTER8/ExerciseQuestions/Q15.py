import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, breaker, container, F_point, S_point
    if (breaker == 0) & (event == cv2.EVENT_LBUTTONDOWN):
        F_point = (x, y)
        container.append(F_point)
        breaker += 1


    if (breaker == 1) & (event == cv2.EVENT_LBUTTONUP):
        S_point = (x, y)
        container.append(S_point)
        breaker += 1

        angle = cv2.fastAtan2(-int(cv2.subtract(F_point, S_point)[0]), -int(cv2.subtract(F_point, S_point)[1]))

        rot_mat = cv2.getRotationMatrix2D((0, 0), -angle, 1)
        dst = cv2.warpAffine(image, rot_mat, (image.shape[::-1][1], image.shape[::-1][2]), cv2.INTER_LINEAR)

        cv2.imshow(title, dst)


        ## 다 초기화
        breaker = 0
        container = []
        F_point, S_point = 0, 0

image = cv2.imread("images/Q13.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

breaker = 0
container = []
F_point, S_point = 0, 0

title = "Q13"


cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)

## 차분을 Atan2 함수로 라디안
## rotation