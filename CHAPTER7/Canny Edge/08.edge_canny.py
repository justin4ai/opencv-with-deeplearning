import numpy as np, cv2

def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # 관심 영역 참조 통해 이웃 화소 가져오기
            values = sobel[i-1:i+2, j-1:j+2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8-id]

            # if문으로 이웃 화소 가져오기
            # if direct[i, j] == 0:
            #   v1, v2 = sobel[i, j-1], sobel[i, j+1]
            # if direct[i, j] == 1:
            #   v1, v2 = sobel[i-1,j-1], sobel[i+1,j+1]
            # if direct[i, j] == 2:
            #   v1, v2 = sobel[i-1,j], sobel[i+1,j]
            # if direct[i, j] == 3:
            #   v1, v2 = sobel[i+1,j-1], sobel[i-1,j+1]

            dst[i, j] = sobel[i, j] if(v1 < sobel[i,j] > v2) else 0 # 최대치 억제
        return dst

def trace(max_sobel, i, j, low):
    h, w = max_sobel.shape
    if (0 <= i < h and 0<= j < w) == False: return
    if pos_ck[i, j] > 0 and max_sobel[i, j] > low:
        pos_ck[i, j] = 255
        canny[i, j] = 255

        trace(max_sobel, i - 1, j - 1, low)
        trace(max_sobel, i, j - 1, low)
        trace(max_sobel, i + 1, j - 1, low)
        trace(max_sobel, i - 1, j, low)
        trace(max_sobel, i + 1, j, low)
        trace(max_sobel, i - 1, j + 1, low)
        trace(max_sobel, i, j + 1, low)
        trace(max_sobel, i + 1, j + 1, low)

def hysteresis_th(max_sobel, low, high):
    rows, cols = max_sobel.shape[:2]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if max_sobel[i, j] >= high: trace(max_sobel, i, j, low)

image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

pos_ck = np.zeros(image.shape[:2], np.uint8)
canny = np.zeros(image.shape[:2], np.uint8)

# 캐니 에지 검출
gaus_img = cv2.GaussianBlur(image, (5, 5), 0.3)
Gx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3)
Gy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3)
sobel = cv2.magnitude(Gx, Gy)

directs = cv2.phase(Gx, Gy) / (np.pi/4)
directs = directs.astype(int) % 4
max_sobel = nonmax_suppression(sobel, directs)
hysteresis_th(max_sobel, 100, 150)

canny = max_sobel.copy()

canny2 = cv2.Canny(image, 100, 150)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("OpenCV_Canny", canny2)
cv2.waitKey(0)


