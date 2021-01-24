import numpy as np, cv2

image = cv2.imread("images/perspective.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

pts1 = np.float32([(70, 50), (360, 193), (25, 340), (385, 380)])    # 입력 영상 4개 좌표
pts2 = np.float32([(50, 60), (340, 60), (50, 320), (360, 320)])     # 목적 영상 4개 좌표

perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)  # 원근 변환 행렬
dst = cv2.warpPerspective(image, perspect_mat, image.shape[1::-1], cv2.INTER_CUBIC)
print("[perspect_mat] = \n%s\n" % perspect_mat)

## 변환 좌표 계산 - 행렬 내적 이용 방법
ones = np.ones((4, 1), np.float64)
pts3 = np.append(pts1, ones, axis=1)    # 원본 좌표 - 동차 좌표 저장
pts4 = cv2.gemm(pts3, perspect_mat.T, 1, None, 1)   # 좌표 변환값 계산

print(" 원본 영상 좌표 \t 목적 영상 좌표 \t\t 동차 좌표 \t\t 변환 결과 좌표")
for i in range(len(pts4)):
    pts4[i] /= pts4[i][2]   # 동차 좌표 -> 직교 좌표
    print("%i : %-14s %-14s %-18s %-18s" % (i, pts1[i], pts2[i], pts3[i], pts4[i]))
    cv2.circle(image, tuple(pts1[i].astype(int)), 3, (0, 255, 0), -1)
    cv2.circle(dst, tuple(pts2[i].astype(int)), 3, (0, 255, 0), -1)

cv2.imshow("image", image)
cv2.imshow("dst_perspective", dst)
cv2.waitKey(0)
