import numpy as np, cv2

image = cv2.imread("images/Q14.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def Thresh1(pos):
    global title, th1
    th1 = pos
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow(title, canny)

def Thresh2(pos):
    global title, th2
    th2 = pos
    canny = cv2.Canny(image, th1, th2)
    cv2.imshow(title, canny)

title = "Canny_Edge"
tth1 = "th1"
tth2 = "th2"

th1 = 100
th2 = 150

canny = cv2.Canny(image, th1, th2)
cv2.imshow(title, canny)

cv2.createTrackbar(tth1, title, th1, 255, Thresh1)
cv2.createTrackbar(tth2, title, th2, 255, Thresh2)

cv2.waitKey(0)

