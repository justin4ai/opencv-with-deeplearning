import numpy as np, cv2

image = cv2.imread("images/Q12.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

gaus1 = cv2.GaussianBlur(image, (3, 3), 0)
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)


Laplacian = cv2.Laplacian(image, cv2.CV_16S, 1)   # 1 : 3x3 기본 마스크
DoG = (gaus1 - gaus2).astype('uint8')

titles = ["Laplacian", "DoG"]
for t in titles:
    cv2.imshow(t, cv2.convertScaleAbs(eval(t)))
cv2.waitKey(0)