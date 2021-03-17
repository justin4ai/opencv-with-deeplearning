import numpy as np, cv2

def nonmax_suppression(sobel, direct):
    rows, cols = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # 관심 영역 참조 통해 이웃 화소 가져오기
            values = sobel[i-1:i+2, j-1:j+2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8-id]

            # # if문으로 이웃 화소 가져오기
            # if direct[i, j] == 0:
            #     v1, v2 = sobel[i, j-1], sobel[i, j+1]
            # if direct[i, j] == 1:
            #     v1, v2 = sobel[i-1, j-1], sobel[i+1, j+1]
            # if direct[i, j] == 2:
            #     v1, v2 = sobel[i-1, j], sobel[i+1, j]
            # if direct[i, j] == 3:
            #     v1, v2 = sobel[i+1, j-1], sobel[i-1, j+1]

            # dst[i, j] = sobel[i, j] if (v1 < sobel[i, j]) & (v2 < sobel[i, j]) else 0
            dst[i, j] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0
    return dst

def trace(max_sobel, i, j, low):
    h, w = max_sobel.shape
    if (0 <= i < h and 0 <= j < w) == False: return
    if pos_ck[i, j] > 0 and max_sobel[i, j] > low:
        pos_ck[i, j] = 255
        canny[i, j] = 255

        trace(max_sobel, i-1, j-1, low)
        trace(max_sobel, i, j-1, low)
        trace(max_sobel, i+1, j-1, low)
        trace(max_sobel, i-1, j, low)
        trace(max_sobel, i+1, j, low)
        trace(max_sobel, i-1, j+1, low)
        trace(max_sobel, i, j+1, low)
        trace(max_sobel, i+1, j+1, low)

def hysteresis_th(max_sobel, low, high):
    rows, cols = max_sobel.shape[:2]
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if max_sobel[i, j] >= high: trace(max_sobel, i, j, low)

image = cv2.imread("images/canny2.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (321, 600))

image_c = cv2.imread("images/canny2.jpg", cv2.IMREAD_COLOR)
image_c = cv2.resize(image_c, (321, 600))
cv2.imshow("color", image_c)

if image is None: raise Exception("영상파일 읽기 오류")

pos_ck = np.zeros(image.shape[:2], np.uint8)
canny = np.zeros(image.shape[:2], np.uint8)

# 캐니 에지 검출
gaus_img = cv2.GaussianBlur(image, (5, 5), 0.3)
cv2.imshow("gaussian", gaus_img)
Gx = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 1, 0, 3)
Gy = cv2.Sobel(np.float32(gaus_img), cv2.CV_32F, 0, 1, 3)

# Gx = cv2.convertScaleAbs(Gx)
# Gy = cv2.convertScaleAbs(Gy)

sobel = cv2.magnitude(Gx, Gy)
sobel = np.clip(sobel, 0, 255).astype(np.uint8)
print(f"<sobel>\n화소값 총합 : {cv2.sumElems(sobel)} \n화소 최대값 : {np.max(sobel)} \n화소 최소값 : {np.min(sobel)} \n행렬 형태 : {sobel.shape}")

directs = cv2.phase(Gx, Gy) / (np.pi/4)
directs = directs.astype(int) % 4
max_sobel = nonmax_suppression(sobel, directs)
max_sobel = max_sobel.astype(np.uint8)
print(f"<max_sobel>\n화소값 총합 : {cv2.sumElems(max_sobel)} \n화소 최대값 : {np.max(max_sobel)} \n화소 최소값 : {np.min(max_sobel)} \n행렬 형태 : {max_sobel.shape}")

cv2.imshow("nonmax_suppression", max_sobel)
# cv2.waitKey(0)

print(sobel >= max_sobel)
checker = sobel >= max_sobel
unique, counts = np.unique(checker, return_counts=True)
checker = dict(zip(unique, counts))
print(checker)

m = 0
n = 0
print(f"sobel의 화소값 : {sobel[m, n]} \nmax_sobel의 화소값 : {max_sobel[m, n]}")

##################
nonmax = max_sobel.copy()


hysteresis_th(max_sobel, 100, 150)

print(nonmax)
print(max_sobel)
print(nonmax == max_sobel)

canny = max_sobel.copy()
canny2 = cv2.Canny(image, 100, 150)

cv2.imshow("image", image)
cv2.imshow("sobel", sobel)
cv2.imshow("canny", canny)
cv2.imshow("OpenCV_Canny", canny2)
cv2.waitKey(0)












































