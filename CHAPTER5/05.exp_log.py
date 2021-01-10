import numpy as np, cv2

v1 = np.array([1, 2, 3], np.float32)
v2 = np.array([[1], [2], [3]], np.float32) #열벡터
v3 = np.array([[1, 2, 3]], np.float32) # 행벡터

v1_exp = cv2.exp(v1)
v2_exp = cv2.exp(v2)
v3_exp = cv2.exp(v3)
v_log = cv2.log(v1)
m_sqrt = cv2.sqrt(v2)
m_pow = cv2.pow(v3, 3)

print("[v1] 형태 : %s 원소: %s" % (v1.shape, v1))
print("[v2] 형태 : %s 원소: %s" % (v2.shape, v2))
print("[v3] 형태 : %s 원소: %s" % (v3.shape, v3))

print("[v1_exp] 자료형 : %s 형태 : %s" % (type(v1_exp), v1_exp.shape))
print("[v2_exp] 자료형 : %s 형태 : %s" % (type(v2_exp), v2_exp.shape))
print("[v3_exp] 자료형 : %s 형태 : %s" % (type(v3_exp), v3_exp.shape))

print("[log] =", v_log.T)
print("[sqrt] =", np.ravel(m_sqrt))
print("[pow] =", m_pow.flatten())