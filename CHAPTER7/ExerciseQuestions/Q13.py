import numpy as np, cv2

image = cv2.imread("images/Q12.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

Average = cv2.blur(src = image, ksize = (3, 3), anchor = (-1, -1), borderType = cv2.BORDER_REFLECT)
Median = cv2.medianBlur(image, 3)
Gaussian = cv2.GaussianBlur(image, (3, 3), 0)


titles = ["Average", "Median", "Gaussian"]
for t in titles:
    cv2.imshow(t, cv2.convertScaleAbs(eval(t)))
cv2.waitKey(0)