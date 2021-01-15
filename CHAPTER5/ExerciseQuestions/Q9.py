import numpy as np, cv2

mat = np.full((3, 6), 100, np.uint8)

# dim : 0 - 열 방향으로 연산하여 1행으로 축소 / 1 - 행 방향으로 축소하여 1열로 축소
row_dst = cv2.reduce(mat, 0, cv2.REDUCE_AVG)
col_dst = cv2.reduce(mat, 1, cv2.REDUCE_AVG)

print("[가로 방향 감축 평균] : {}".format(col_dst))
print("[세로 방향 감축 평균] : {}".format(row_dst))
