import numpy as np
import cv2

image1 = np.zeros((50, 512), np.float32)
print(image1[0][0])
#image2 = np.zeros((50, 512), np.uint8)
rows, cols = image1.shape[:2]

for i in range(rows):
    for j in range(cols):
        image1.itemset((i, j), (1 - j/512))
        #image2.itemset((i, j), j // 20*10)

print(image1)

cv2.imshow("image1", image1)
#cv2.imshow("image2", image2)
cv2.waitKey(0)