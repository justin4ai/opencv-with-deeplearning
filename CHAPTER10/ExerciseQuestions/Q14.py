import numpy as np, cv2

def morphing():     # 드래그 거리만큼 영상 왜곡
    h, w = image.shape[:2]
    dst = np.zeros((h, w), image.dtype) # 반환 영상
    ys = np.arange(0, image.shape[0], 0.1)        # y 좌표 인덱스
    xs = np.arange(0, image.shape[1], 0.1)      # x 좌표 인덱스 (0.1 간격)

    x1, x10 = pt1[0], pt1[0] * 10       # 0.1 간격의 10배 -> 정수 인덱스 구성
    y1, y10 = pt1[1], pt1[1] * 10
    ratios_x = xs / x1        # 기본 변경 비율
    ratios_y = ys / y1

    ratios_x[x10:] = (w - xs[x10:]) / (w - x1)        # x 좌표 이상은 다른 비율 적용
    ratios_y[y10:] = (h - ys[y10:]) / (h - y1)

    dxs = xs + ratios_x * (pt2[0] - pt1[0])       # 변경 좌표 인덱스 생성
    dys = ys + ratios_y * (pt2[1] - pt1[1])

    xs, dxs = xs.astype(int), dxs.astype(int)       # 좌표를 정수값으로 변경
    ys, dys = ys.astype(int), dys.astype(int)


    ym, xm = np.meshgrid(ys, xs)        # 원본 좌표 정방행렬
    dym, dxm = np.meshgrid(dys, dxs)       # 변경 좌표 정방행렬
    dst[dym, dxm] = image[ym, xm]        # 원본 좌표를 목적 좌표로 매칭
    cv2.imshow("image", dst)

def onMouse(event, x, y, flags, param):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)        # 드래그 시작 좌표

    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)        # 드래그 종료 좌표
        morphing()
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        pt1 = pt2 = (-1, -1)
        cv2.imshow("image", image)      # 원상복구

image = cv2.imread("images/Q14.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

pt1 = pt2 = (-1, -1)
cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)