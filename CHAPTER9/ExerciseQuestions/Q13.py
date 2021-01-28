import numpy as np, cv2
# from Common.fft2d import FFT, IFFT, calc_spectrum
import math

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

image = cv2.imread("images/Q13.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")
cy, cx = np.divmod(image.shape, 2)[0]       # 행렬 중심점 구하기
mode = 3        # FFT 방법 선택

dft, spectrum = FFT(image, mode)        # FFT 수행 및 셔플링
# lowpass = np.zeros(dft.shape, np.float32)   # 저주파 통과 필터
midpass = np.zeros(dft.shape, np.float32)   # 중대역 통과 필터
# highpass = np.ones(dft.shape, np.float32)   # 고주파 통과 필터

#cv2.circle(lowpass, (cx, cy), 30, (1, 1),-1)    # 2개 채널로 값 지정
cv2.circle(midpass, (cx, cy), 90, (1, 1), 60)
#cv2.circle(highpass, (cx, cy), 30, (0, 0),-1)    # 2개 채널로 값 지정

# lowpassed_dft = dft * lowpass   # 주파수 필터링
midpassed_dft = dft * midpass
# highpassed_dft = dft * highpass
# lowpassed_img = IFFT(lowpassed_dft, image.shape, mode)  # 푸리에 역변환
midpassed_img = IFFT(midpassed_dft, image.shape, mode)
# highpassed_img = IFFT(highpassed_dft, image.shape, mode)

cv2.imshow("image", image)
# cv2.imshow("lowpassed_img", lowpassed_img)
cv2.imshow("midpassed_img", midpassed_img)
# cv2.imshow("highpassed_img", highpassed_img)
cv2.imshow("spectrum_img", spectrum)
# cv2.imshow("lowpass_spect", calc_spectrum(lowpassed_dft))
cv2.imshow("midpassed_spect", calc_spectrum(midpassed_dft))
# cv2.imshow("highpass_spect", calc_spectrum(highpassed_dft))
cv2.waitKey(0)