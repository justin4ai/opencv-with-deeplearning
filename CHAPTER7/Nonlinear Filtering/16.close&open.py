import numpy as np, cv2
from Common.filters import erode, dilate

def opening(img, mask):
    tmp = erode(img, mask)
    dst = dilate(tmp, mask)
    return dst

def closing(img, mask):
    tmp = dilate(img, mask)
    dst = erode(tmp, mask)
    return dst

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0,
                  1, 1, 1,
                  0, 1, 0]]).astype('uint8')
th_img = cv2.threshold(image, 139, 255, cv2.THRESH_BINARY)[1]   # 원래 180 대신 128

dst1 = opening(th_img, mask)
dst2 = closing(th_img, mask)
dst3 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask)
dst4 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations = 1 ) # iterations로 반복 횟수 지정

cv2.imshow("User_opening", dst1);   cv2.imshow("User_closing", dst2)
cv2.imshow("OpenCV_opening", dst3);     cv2.imshow("OpenCV_closing", dst4)
cv2.waitKey(0)