import numpy as np, cv2

def getGaussianMask(ksize, sigmaX, sigmaY): # ksize : kernel size
    sigma = 0.3 * ((np.array(ksize) - 1.0) * 0.5 - 1.0) + 0.8
    if sigmaX <= 0: sigmaX = sigma[0]
    if sigmaY <= 0: sigmaY = sigma[1]

    u = np.array(ksize)//2
    x = np.arange(-u[0], u[0]+1, 1) # 평균을 중심으로 커널 크기에 맞게 1 간격의 범위 생성
    y = np.arange(-u[1], u[1]+1, 1)
    x, y = np.meshgrid(x, y) # 각각 x, y방향 정방행렬

    ## 가우시안 함수의 세부 공식을 곱해서 계수 생성
    ratio = 1 / (sigmaX * sigmaX * 2 * np.pi)
    v1 = x ** 2 / (2 * sigmaX ** 2)
    v2 = y ** 2 / (2 * sigmaY ** 2)
    mask = ratio * np.exp(-(v1 + v2))   # 2차원 정규분포
    return mask / np.sum(mask)  # 원소 전체 합 1 유지

image = cv2.imread("images/smoothing.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

ksize = (17, 5)
gaussian_2d = getGaussianMask(ksize, 0, 0)
gaussian_1dx = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)   # 가로방향 마스크
gaussian_1dy = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)

gauss_img1 = cv2.filter2D(image, -1, gaussian_2d)   # 사용자 생성 마스크 적용
gauss_img2 = cv2.GaussianBlur(image, ksize, 0)
gauss_img3 = cv2.sepFilter2D(image, -1, gaussian_1dx, gaussian_1dy)

titles = ['image', 'gauss_img1', 'gauss_img2', 'gauss_img3']
for t in titles:    cv2.imshow(t, eval(t))
cv2.waitKey(0)
