import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title, breaker, container, F_point, S_point
    if (breaker == 0) & (event == cv2.EVENT_LBUTTONDOWN):
        F_point = (x, y)
        container.append(F_point)
        breaker += 1
        print(container)

    if (breaker == 1) & (event == cv2.EVENT_LBUTTONUP):
        S_point = (x, y)
        container.append(S_point)
        breaker += 1
        print(container)

    # if breaker == 2:
        pts = np.array(container).astype(int)
        print([pts])
        cv2.line(image, F_point, S_point, (0, 255, 255), 10)
        #cv2.polylines(image, [pts], True, (0, 255, 255), 10)
        cv2.imshow(title, image)


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