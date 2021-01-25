import numpy as np, math, cv2

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1]-1: x = x - 1
    if y >= img.shape[0]-1: y = y - 1
    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten()) # 관심 영역으로 접근

    alpha, beta = pt[1] - y, pt[0] - x  # 거리 비율
    M1 = P1 + alpha * (P3 - P1) # 1차 보간
    M2 = P2 + alpha * (P4 - P2)

    P = M1 + beta * (M2 - M2)   # 2차 보간
    return np.clip(P, 0, 255)   # 화소값 saturation 후 반환

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def rotate_pt(img, degree, pt): # pt 기준 회전 변환 함수
    dst = np.array([np.zeros(img.shape[:2], img.dtype) for i in range(3)])
    radian = (degree/180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    b, g, r = cv2.split(image)
    tmplist = np.array([b, g, r])

    for d in range(len(dst)):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                jj, ii = np.subtract((j, i), pt)
                y = -jj * sin + ii * cos
                x = jj * cos + ii * sin
                x, y = np.add((x, y), pt)   # 중심 좌표로 평행 이동
                if contain((y, x), img.shape[:2]):
                    dst[d][i, j] = bilinear_value(tmplist[d], (x, y)) # 화소값 양선형 보간

    return cv2.merge(dst)

image = cv2.imread("images/Q12.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

center = np.divmod(image.shape[:2][::-1], 2)[0]

dst2 = rotate_pt(image, 20, center)

cv2.imshow("image", image)
cv2.imshow("dst2 : rotated on center point", dst2)
cv2.waitKey(0)