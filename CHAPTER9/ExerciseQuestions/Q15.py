import numpy as np, cv2
# from Common.fft2d import FFT, IFFT, calc_spectrum
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2
    dst[h - cy:, w - cx:] = np.copy(img[0 : cy, 0 : cx])
    dst[0:cy, 0:cx] = np.copy(img[h - cy:, w - cx:])
    dst[0:cy, w - cx:] = np.copy(img[h - cy:, 0:cx])
    dst[h - cy:, 0:cx] = np.copy(img[0:cy, w - cx:])
    return dst

def butterfly(pair, L, N, dir):
    for k in range(L):
        Geven, Godd = pair[k], pair[k + L]
        pair[k] = Geven + Godd * exp(dir * k / N)   # 짝수부
        pair[k + L] = Geven - Godd * exp(dir * k / N)   # 홀수부

def pairing(g, N, dir, start = 0, stride = 1):  # 2원소까지 재귀 통한 분리 / 합성
    if N == 1: return [g[start]]
    L = N // 2
    sd = stride * 2
    part1 = pairing(g, L, dir, start, sd)   # 홀수 신호 재귀 분리
    part2 = pairing(g, L, dir, start + stride, sd)  # 짝수신호 재귀 분리
    pair = part1 + part2
    butterfly(pair, L, N, dir)  # 버터플라이 수행
    return pair

def fft(g):     # 1차원 fft 수행
    return pairing(g, len(g), 1)

def ifft(g):        # 1차원 ifft 수행
    fft = pairing(g, len(g), -1)
    return [v / len(g) for v in fft]

def fft2(image):
    pad_img = zeropadding(image)
    tmp = [fft(row) for row in pad_img]
    dst = [fft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def ifft2(image):
    tmp = [ifft(row) for row in image]
    dst = [ifft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def exp(knN):
    th = -2 * math.pi * knN     # 푸리에 변환 각도값
    return complex(math.cos(th), math.sin(th))  # 복소수 클래스

def zeropadding(img):
    h, w = img.shape[:2]
    m = 1 << int(np.ceil(np.log2(h)))   # 2의 자승 계산
    n = 1 << int(np.ceil(np.log2(w)))
    dst = np.zeros((m, n), img.dtype)
    dst[0:h, 0:w] = img[:]  # 자승 크기 영상에 원본 영상 복사
    return dst

def calc_spectrum(complex):
    if complex.ndim == 2:
        dst = abs(complex)
    else :
        dst = cv2.magnitude(complex[:, :, 0], complex[:, :, 1])
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

def FFT(image, mode = 2):
    if mode == 1: dft = fft2(image) # 저자 구현 함수
    elif mode == 2: dft = np.fft.fft2(image)    # 넘파이 함수
    elif mode == 3: dft = cv2.dft(np.float32(image), flags = cv2.DFT_COMPLEX_OUTPUT)
    dft = fftshift(dft)
    spectrum = calc_spectrum(dft)
    return dft, spectrum

def IFFT(dft, shape, mode = 2):
    dft = fftshift(dft)     # 역 시프트
    if mode == 1: img = ifft2(dft).real
    if mode == 2: img = np.fft.ifft2(dft).real
    if mode == 3: img = cv2.idft(dft, flags = cv2.DFT_SCALE)[:, :, 0]
    img = img[:shape[0], :shape[1]]     # 영삽입 부분 제거
    return cv2.convertScaleAbs(img)     # 절대값 및 uint8 스케일링

def get_gaussianFilter(shape, R):       # 가우시안 필터 함수
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)    # x, y 좌표 정방행렬 생성
    filter = np.exp(-(x**2 + y**2) / (2 * R**2))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

def get_butterworthFilter(shape, R, n):     # 버터워스 필터 생성 함수
    u = np.array(shape) // 2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)  # x, y 좌표 정방행렬 생성
    dist = np.sqrt(x**2 + y**2)
    filter = 1 / (1 + np.power(dist / R, 2 * n))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

image = cv2.imread("images/Q15.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

mode = 2
dft, spectrum = FFT(image, mode)    # FFT 수행 및 셔플링 진행
x1, y1, gauss_filter = get_gaussianFilter(dft.shape, 30)        # 필터 생성
x2, y2, butter_filter = get_butterworthFilter(dft.shape, 30, 10)

if mode == 3:
    gauss_filter, butter_filter = gauss_filter[:, :, 0], butter_filter[:, :, :]     # OpenCV 함수는 2채널 사용

fig = plt.figure(figsize = (10, 10))
# ax1 = plt.subplot(332, projection = '3d')
# ax1.plot_surface(x1, y1, gauss_filter, cmap="RdPu"), plt.title("gauss_filter")
# ax2 = plt.subplot(333, projection = '3d')
# ax2.plot_surface(x2, y2, butter_filter, cmap = 'RdPu'), plt.title("butter_filter")

ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x2, y2, butter_filter, cmap = 'RdPu')
plt.tight_layout(), plt.show()