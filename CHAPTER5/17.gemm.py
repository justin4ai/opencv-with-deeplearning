import numpy as np, cv2

src1 = np.array([1, 2, 3, 1, 2, 3], np.float32).reshape(2, 3)
src2 = np.array([1, 2, 3, 4, 5, 6], np.float32).reshape(2, 3)
src3 = np.array([1, 2, 1, 2, 1, 2], np.float32).reshape(3, 2)
alpha, beta = 1.0, 1.0

dst1 = cv2.gemm(src1, src2, alpha, None, beta, flags=cv2.GEMM_1_T)  # 첫 인수 전치후 행렬 내적
dst2 = cv2.gemm(src1, src2, alpha, None, beta, flags=cv2.GEMM_2_T)  # alpha : src1.T dot src2 에 대한 가중치 // beta : src3(앞 행렬곱에 더해지는 델타 행렬) 행렬에 곱해지는 가중치
dst3 = cv2.gemm(src1, src3, alpha, None, beta)

titles = ['src1', 'src2', 'src3', 'dst1', 'dst2', 'dst3']
for title in titles:
    print("[%s] = \n%s\n" % (title, eval(title)))