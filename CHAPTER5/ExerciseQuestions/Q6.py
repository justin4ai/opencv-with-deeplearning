''' 원문
import numpy as np, cv2

m1 = [1, 2, 3, 1, 2, 3]
m2 = [3, 3, 4, 2, 2, 3]
m3 = m1 + m2
m4 = m1 - m2

print("[m1] = %s" %m1)
print("[m2] = %s" %m2)
print("[m3] = %s" %m3)
print("[m4] = %s" %m4)'''

import numpy as np, cv2

m1 = np.array([1, 2, 3, 1, 2, 3])
m2 = np.array([3, 3, 4, 2, 2, 3])
m3 = cv2.add(m1, m2)
m4 = cv2.subtract(m1, m2)

print("[m1] = %s" %m1)
print("[m2] = %s" %m2)
print("[m3] = %s" %m3)
print("[m4] = %s" %m4)

######################################################################################
######################################################################################

''' 원문
import numpy as np, cv2

data = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10, 11, 12]
m1= np.array(data).reshape(2, 3, 2)

print(m1.shape)
r, g, b = cv2.split(m1)

print("[m1] = %s" %m1 )
print("[r, g, b] = %s, %s, %s" %(r, g, b))'''

import numpy as np, cv2

data = [1, 2, 3, 4, 5,  6, 7, 8, 9, 10, 11, 12]
m1= np.array(data).reshape(2, 2, 3)

print(m1.shape)
r, g, b = cv2.split(m1)

print("[m1] = %s" %m1 )
print("[r, g, b] = %s, %s, %s" %(r, g, b))