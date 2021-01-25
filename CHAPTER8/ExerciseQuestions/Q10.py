import numpy as np, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]    # 좌표 내에 있는지 없는지

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)    # 목적 영상 생성
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x, y = np.subtract((j, i), pt)  # 좌표는 가로, 세로 순서
            if contain((y, x), img.shape):
                dst[i, j] = img[y, x]   # 행렬은 행, 열 순서

    return dst


image = cv2.imread("images/Q10.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

size = image.shape[::-1]
print(size)


trans_mat = np.float32([[1,0,50],[0,1,60]])


dst1 = translate(image, (50, 60))
dst2 = cv2.warpAffine(image, trans_mat, size, cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("dst1: translated to (50, 60) using User function", dst1)
cv2.imshow("dst2: translated to (50, 60) using OpenCV", dst2)
cv2.waitKey(0)