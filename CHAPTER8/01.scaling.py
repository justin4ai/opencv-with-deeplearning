import numpy as np, cv2
import time

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)   # size와 shape는 원소 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)   # 입력 영상 세로 좌표 생성
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)   # 목적 영상 좌표
    dst[i, j] = img[y, x]   # 정방향 사상 -> 목적 영상 좌표 계산
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)
            dst[i, j] = img[y, x]
    return dst

def time_check(func, image, size, title):
    start_time = time.perf_counter()
    ret_img = func(image, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(title, "수행시간 = %0.2f ms" % elapsed)
    return ret_img

image = cv2.imread("images/scaling.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

dst1 = scaling(image, (150, 200))
dst2 = scaling2(image, (150, 200))
dst3 = time_check(scaling, image, (300, 400), "[방법1]: 정방행렬 방식")
dst4 = time_check(scaling2, image, (300, 400), "[방법2]: 반복문 형식")

cv2.imshow("image", image)
cv2.imshow("dst1 - zoom out", dst1)
cv2.imshow("dst3 - zoom out", dst3)
cv2.resizeWindow("dst1 - zoom out", 260, 200)
cv2.waitKey(0)