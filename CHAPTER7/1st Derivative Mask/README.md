<h1> ● Sobel Mask </h1>
<br>
   
## 1) How the Mask Consist


<p align="center"><img src="https://i0.wp.com/www.adeveloperdiary.com/wp-content/uploads/2019/05/How-to-implement-Sobel-edge-detection-using-Python-from-scratch-adeveloperdiary.com-sobel-sobel-operator.jpg?resize=744%2C356"></img>
<img src="https://i2.wp.com/theailearner.com/wp-content/uploads/2019/05/gradien.png?resize=419%2C132&ssl=1"></img></p>      



        
## 2) After applying?

<p align="center"><img src="https://www.tutorialspoint.com/dip/images/sobel3.jpg"></img></p> 

:)

```python

import numpy as np, cv2

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [ -1, 0, 1,
          -2, 0, 2,
          -1, 0, 1]

data2 = [ -1, -2, -1,
           0,  0,  0,
           1,  2,  1]

dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3) # 1 : x방향
dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3) # 1 : y방향
dst3 = cv2.convertScaleAbs(dst3)    # 절댓값 및 uint8 형변환
dst4 = cv2.convertScaleAbs(dst4)

cv2.imshow("dst3- vertical_OpenCV", dst3)
cv2.imshow("dst4- horizontal_OpenCV", dst4)
cv2.waitKey(0)
```
