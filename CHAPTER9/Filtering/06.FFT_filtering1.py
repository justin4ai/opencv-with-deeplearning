import numpy as np, cv2
from Common.fft2d import fft2, ifft2, calc_spectrum, fftshift

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

image = cv2.imread("images/filter.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")
cy, cx = np.divmod(image.shape, 2)[0]       # 행렬 중심점 구하기
mode = 3        # FFT 방법 선택

dft, spectrum = FFT(image, mode)        # FFT 수행 및 셔플링
lowpass = np.zeros(dft.shape, np.float32)   # 저주파 통과 필터
highpass = np.ones(dft.shape, np.float32)   # 고주파 통과 필터
cv2.circle(lowpass, (cx, cy), 30, (1, 1),-1)    # 2개 채널로 값 지정
cv2.circle(highpass, (cx, cy), 30, (0, 0),-1)    # 2개 채널로 값 지정

lowpassed_dft = dft * lowpass   # 주파수 필터링
highpassed_dft = dft * highpass
lowpassed_img = IFFT(lowpassed_dft, image.shape, mode)  # 푸리에 역변환
highpassed_img = IFFT(highpassed_dft, image.shape, mode)

cv2.imshow("image", image)
cv2.imshow("lowpassed_img", lowpassed_img)
cv2.imshow("highpassed_img", highpassed_img)
cv2.imshow("spectrum_img", spectrum)
cv2.imshow("lowpass_spect", calc_spectrum(lowpassed_dft))
cv2.imshow("highpass_spect", calc_spectrum(highpassed_dft))
cv2.waitKey(0)