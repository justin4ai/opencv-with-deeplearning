import numpy as np, cv2
from Common.interpolation import contain, bilinear_value

def affine_transform(img, mat):
    rows, cols = img.shape[:2]
    inv_mat = cv2.invertAffineTransform(mat)    # 어파인 변환의 역행렬

    ## 리스트 생성 방식
    pts = [np.dot(inv_mat, (j, i, 1)) for i in range(rows) for j in range(cols)]
    dst = [bilinear_value(img, p) if contain(p, size) else 0 for p in pts]
    dst = np.reshape(dst, (rows, cols)).astype("uint8")

    return dst

image = cv2.imread("images/affine.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

center = (200, 200)
angle, scale = 30, 1    # 30도 회전, 크기 변경 안 함
size = image.shape[::-1]

pt1 = np.array([(30, 70), (20, 240), (300, 110)], np.float32)
pt2 = np.array([(120, 20), (10, 180), (280, 260)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)  # 3개 좌표쌍 어파인 행렬 생성
rot_mat = cv2.getRotationMatrix2D(center, angle, scale) # 어파인 행렬

dst1 = affine_transform(image, aff_mat)
dst2 = affine_transform(image, rot_mat)
dst3 = cv2.warpAffine(image, aff_mat, size, cv2.INTER_LINEAR)
dst4 = cv2.warpAffine(image, rot_mat, size, cv2.INTER_LINEAR)

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
dst1 = cv2.cvtColor(dst1, cv2.COLOR_GRAY2BGR)
dst3 = cv2.cvtColor(dst3, cv2.COLOR_GRAY2BGR)

for i in range(len(pt1)):
    cv2.circle(image, tuple(pt1[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst1, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)
    cv2.circle(dst3, tuple(pt2[i].astype(int)), 3, (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.imshow("dst1_affine", dst1)
cv2.imshow("dst2_affine_rotate", dst2)
cv2.imshow("dst3_OpenCV_affine", dst3)
cv2.imshow("dst4_OpenCV_affine_rotate", dst4)
cv2.waitKey(0)
