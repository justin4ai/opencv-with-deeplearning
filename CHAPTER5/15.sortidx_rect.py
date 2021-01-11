import numpy as np, cv2

def print_rects(rects):
    print("-" * 46)
    print("사각형 원소\t\t랜덤 사각형 정보\t 크기")
    print("-" * 46)
    for i, (x, y, w, h, a) in enumerate(rects):
        print("rects[%i] = [(%3d, %3d) from (%3d, %3d)] %5d" %(i, x, y, w, h, a))

rands = np.zeros((5, 5), np.uint16)
starts = cv2.randn(rands[:, :2], 100, 50)    # 시작 좌표(0, 1열) 랜덤 생성
ends = cv2.randn(rands[:, 2:-1], 300, 50)   # 종료 좌표(2, 3열) 랜덤 생성

sizes = cv2.absdiff(starts, ends)
areas = sizes[:, 0] * sizes[:, 1]
rects = rands.copy()
rects[:, 2:-1] = sizes  # 2열, 3열에 크기(가로, 세로) 저장
rects[:, -1] = areas    # 마지막(-1) 열에 넓이 저장

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()
# idx = np.argsort(areas, axis=0)

print_rects(rects)
print_rects(rects[idx.astype('int')])