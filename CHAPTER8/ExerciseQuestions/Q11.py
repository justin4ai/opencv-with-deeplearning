import numpy as np, math, cv2

def getAffineMat(center, degree, fx=1, fy=1, translate=(0, 0)):
    scale_mat = np.eye(3, dtype=np.float32)     # 크기 변경 행렬
    cen_trans = np.eye(3, dtype=np.float32)     # 중점 평행 이동
    org_trans = np.eye(3, dtype=np.float32)     # 원점 평행 이동
    trans_mat = np.eye(3, dtype=np.float32)     # 좌표 평행 이동
    rot_mat = np.eye(3, dtype=np.float32)       # 회전 변환 행렬

    radian = degree / 180 * np.pi
    rot_mat[0] = [ np.cos(radian), np.sin(radian), 0]   # 회전행렬 0행
    rot_mat[1] = [ -np.sin(radian), np.cos(radian), 0]  # 회전행렬 1행

    cen_trans[:2, 2] = center   # 중심 좌표 이동
    org_trans[:2, 2] = -center[0], -center[1]   # 원점으로 이동
    trans_mat[:2, 2] = translate    # 평행 이동 행렬의 원소 지정
    scale_mat[0, 0], scale_mat[1, 1] = fx, fy

    ret_mat = cen_trans.dot(rot_mat.dot(trans_mat.dot(scale_mat.dot(org_trans))))
    return np.delete(ret_mat, 2, axis = 0)  # 마지막 행 제거

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
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = math.sin(radian), math.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)
            y = -jj * sin + ii * cos
            x = jj * cos + ii * sin
            x, y = np.add((x, y), pt)   # 중심 좌표로 평행 이동
            if contain((y, x), img.shape):
                dst[i, j] = bilinear_value(img, (x, y)) # 화소값 양선형 보간

    return dst

image = cv2.imread("images/Q11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

#center = np.divmod(image.shape[::-1], 2)[0]
center = (100, 100)
dst1 = rotate_pt(image, 30, center)

M = getAffineMat(center, -30)
dst2 = cv2.warpAffine(image, M, image.shape[::-1], cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("dst1 : rotated on center point using User func", dst1)
cv2.imshow("dst2 : rotated on center point using OpenCV", dst2)
cv2.waitKey(0)