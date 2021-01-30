import numpy as np, cv2, math
import scipy.fftpack as sf

def cos(n, k, N):
    return math.cos((n + 1 / 2) * math.pi * k / N)

def C(k, N):        # 상수 계산 함수
    return math.sqrt(1 / N) if k == 0 else math.sqrt(2 / N)

def dct(g):
    N = len(g)
    f = [C(k, N) * sum(g[n] * cos(n, k, N) for n in range(N)) for k in range(N)]
    return np.array(f, np.float32)

def idct(f):
    N = len(f)
    g = [sum(C(k, N) * f[k] * cos(n, k, N) for k in range(N)) for n in range(N)]
    return np.array(g)

def dct2(image):
    tmp = [dct(row) for row in image]
    dst = [dct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def idct2(image):
    tmp = [idct(row) for row in image]
    dst = [idct(row) for row in np.transpose(tmp)]
    return np.transpose(dst)

def scipy_dct2(a):
    tmp = sf.dct(a, axis = 0, norm="ortho")
    return sf.dct(tmp, axis = 1, norm="ortho")

def scipy_idct2(a):
    tmp = sf.idct(a, axis = 0, norm="ortho")
    return sf.idct(tmp, axis = 1, norm="ortho")


def dct2_mode(block, mode):
    if mode==1: return dct2(block)
    elif mode==2: return scipy_dct2(block)
    elif mode==3: return cv2.dct(block.astype('float32'))

def idct2_mode(block, mode):
    if mode==1: return idct2(block)
    elif mode==2: return scipy_idct2(block)
    elif mode==3: return cv2.dct(block, flags=cv2.DCT_INVERSE)

def dct_filtering(img, filter, M, N):
    dst = np.empty(img.shape, np.float32)
    for i in range(0, img.shape[0], M):
        for j in range(0, img.shape[1], N):
            block = img[i:i+M, j:j+N]
            new_block = dct2_mode(block, mode)
            if new_block.shape!=(8,8): continue
            new_block = new_block * filter
            dst[i:i+M, j:j+N] = idct2_mode(new_block, mode)
    return cv2.convertScaleAbs(dst)

image = cv2.imread("images/Q16.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

mode = 1
M, N = 8, 8
filters = [np.zeros((M,N), np.float32) for i in range(5)]
titles = ['DC Pass', 'High Pass', 'Low Pass', 'Vertical Pass', 'Horizontal Pass']

filters[0][0, 0] = 1
filters[1][:], filters[1][0, 0] = 1, 0
filters[2][:M//2, :N//2] = 1
filters[3][1:, 0] = 1
filters[4][0, 1:] = 1

for filter, title in zip(filters, titles):
    dst = dct_filtering(image, filter, M, N)
    cv2.imshow(title, dst)
cv2.imshow("image", image)
cv2.waitKey(0)