import numpy as np, cv2
from Common.dft2d import dft, idft, calc_spectrum, fftshift
import time

def dft2(image):
    tmp = [dft(row) for row in image]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ck_time(mode = 0):  # 수행시간 체크 함수
    global stime    # 함수 내부에서 값 유지위해
    if (mode == 0):
        stime = time.perf_counter()
    elif (mode == 1):
        etime = time.perf_counter()
        print("수행시간 = %.5f sec" % (etime - stime))

image = cv2.imread("images/dft_240.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

ck_time(0)
dft = dft2(image)
spectrum1 = calc_spectrum(dft) # 주파수 스펙트럼 영상
spectrum2 = fftshift(spectrum1)
idft = idft2(dft).real      # 2차원 IDFT 수행
ck_time(1)

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.imshow("spectrum2", spectrum2)
cv2.imshow("idft_img", cv2.convertScaleAbs(idft))