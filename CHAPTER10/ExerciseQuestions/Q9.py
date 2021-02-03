import numpy as np, cv2
import pickle

def accumulate(image, rho, theta):
    h, w = image.shape[:2]
    rows, cols = (h + w) * 2 // rho, int(np.pi / theta)  # 누적행렬 너비, 높이
    accumulate = np.zeros((rows, cols), np.int32)  # 직선 누적행렬

    sin_cos = [(np.sin(t * theta), np.cos(t * theta)) for t in range(cols)]  # 삼각 함수값 저장
    pts = np.where(image > 0)  # 넘파이 함수 활용 - 직선좌표 찾기

    polars = np.dot(sin_cos, pts).T  # 행렬 곱으로 극좌표 계산
    polars = (polars / rho + rows / 2).astype('int')  # 해상도 변경 및 위치 조정

    for row in polars:
        for t, r in enumerate(row):  # 각도, 수직 거리 가져옴
            accumulate[r, t] += 1  # 극좌표에 누적

    return accumulate

image = cv2.imread("images/Q9.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

with open("Q9_.txt", "wb") as f:
    pickle.dump(accumulate(image, 1, 1), f)