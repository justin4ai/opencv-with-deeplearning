import numpy as np
import cv2

image8 = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
if image8 is None: raise Exception("영상파일 읽기 에러")

image16 = np.uint16(image8 * (65535/255))
image32 = np.float32(image8 * (1/255))

## 화소값 확인 - 관심 영역((10, 10) 위치에서 2행, 3열) 출력
print("image8 행렬의 일부\n %s\n" % image8[10:12, 10:13])
print("image16 행렬의 일부\n %s\n" % image16[10:12, 10:13])
print("image32 행렬의 일부\n %s\n" % image32[10:12, 10:13])

cv2.imwrite("images/write_test_16.tif", image16)
cv2.imwrite("images/write_test_32.tif", image32)

cv2.imshow("image16", image16)
cv2.imshow("image32", (image32*255).astype('uint8'))
cv2.waitKey(0)