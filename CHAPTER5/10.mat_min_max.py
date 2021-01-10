import numpy as np, cv2

data = [ 10, 200, 5, 7, 9,  # 1차원 리스트
         15, 35, 60, 80, 710,
         100, 2, 55, 37, 70 ]
m1 = np.reshape(data, (3, 5))   # 3 x 5 2차원 배열로
m2 = np.full((3, 5), 50)

m_min = cv2.min(m1, 30)
m_max = cv2.max(m1, m2)

## 행렬의 최솟값/최댓값과 그 좌표들을 반환
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m1)

print("[m1] = \n%s\n" % m1)
print("[m_min] = \n%s\n" % m_min)
print("[m_max] = \n%s\n" % m_max)

# min_loc와 max_loc 좌표는 (y, x)이므로 행렬의 좌표 위치와 반대임
print("m1 행렬 최솟값 좌표%s, 최솟값: %d" %(min_loc, min_val))
print("m1 행렬 최댓값 좌표%s, 최댓값: %d" %(max_loc, max_val))