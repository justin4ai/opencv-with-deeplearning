import numpy as np, cv2
from Common.interpolation import contain_pts

def draw_rect(img):
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y+h, x:x+w]         # 좌표 사각형 범위 가져오기
        val = np.full(roi.shape, 80, np.uint8)      # 컬러(3차원) 행렬 생성
        cv2.add(roi, val, roi)      # 관심 영역 밝기 증가
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)    # 4개 좌표 잇기
    cv2.imshow("select rect", img)

def warp(img):  # 원근 변환 수행 함수
    perspet_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (350, 400), cv2.INTER_CUBIC)   # 원근 변환
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param): # 마우스 이벤트 처리 함수
    global check
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, p in enumerate(pts1):
            p1, p2 = p - small, p + small   # p 좌표의 우상단, 좌하단 좌표 생성
            if contain_pts((x, y), p1, p2): check = i   # 클릭 좌표로 좌표 사각형 선택

    if event == cv2.EVENT_LBUTTONUP: check = -1     # 마우스 업시 좌표번호 초기화

    if check >= 0:      # 좌표 사각형 선택 시
        pts1[check] = (x, y)
        draw_rect(np.copy(image))
        warp(np.copy(image))

image = cv2.imread("images/perspective.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

small = np.array([12, 12])
check = -1
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])

draw_rect(np.copy(image))
cv2.setMouseCallback("select rect", onMouse, 0)
cv2.waitKey(0)