import numpy as np, cv2
import math

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

def fftshift(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cy, cx = h // 2, w // 2
    dst[h - cy:, w - cx:] = np.copy(img[0 : cy, 0 : cx])
    dst[0:cy, 0:cx] = np.copy(img[h - cy:, w - cx:])
    dst[0:cy, w - cx:] = np.copy(img[h - cy:, 0:cx])
    dst[h - cy:, 0:cx] = np.copy(img[0:cy, w - cx:])
    return dst

image = cv2.imread("images/Q11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

dft1 = fft2(image)

spectrum1 = calc_spectrum(fftshift(dft1))

cv2.imshow("Q11", spectrum1)
cv2.waitKey(0)