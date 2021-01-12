import numpy as np, cv2

theta = 20 * np.pi / 100
rot_mat = np.array([ [np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]], np.float32)

pts1 = np.array([ (250, 30), (400, 70),
                  (350, 250), (150, 200)], np.float32)  # 입력 좌표 지정
pts2 = cv2.gemm(pts1, rot_mat, 1, None, 1, flags=cv2.GEMM_2_T ) # 행렬곱으로 회전변환

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print("[pts1[%d] = %s, pts2[%d]= %s" %(i, pt1, i, pt2))


## 영상 생성 및 4개 좌표 그리기
image = np.full((400, 500, 3), 255, np.uint8)
cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 2)
cv2.imshow('image', image)
cv2.waitKey(0)
