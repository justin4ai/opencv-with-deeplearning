import numpy as np, cv2
from Common.hough import *

def detect_maxObject(img):
    results = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if int(cv2.__version__[0]) >= 4:
        contours = results[0]
    else:
        contours = results[1]

    areas = [cv2.contourArea(c) for c in contours]
    idx = np.argsort(areas)
    max_rect = contours[idx[-1]]

    rect = cv2.boundingRect(max_rect)
    rect = np.add(rect, (-10, -10, 20, 20))
    return rect

image = cv2.imread("images/harness.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

rho, theta = 1, np.pi / 180
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
th_gray = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3,3), np.uint8)
morph = cv2.erode(th_gray, kernel, iterations=2)

x, y, w, h = detect_maxObject(np.copy(morph))
roi = th_gray[y:y+h, x:x+h]

canny = cv2.Canny(roi, 40, 100)
lines = houghLines(canny, rho, theta, 50)
print(lines)
# lines = cv2.HoughLines(canny, rho, theta, 50)

cv2.rectangle(morph, (x, y, w, h), 100, 2)
canny_line = draw_houghLines(canny, lines, 1)

angle = (np.pi - lines[0, 0, 1]) * 180 / np.pi
h, w = image.shape[:2]
center = (w//2, h//2)
rot_map = cv2.getRotationMatrix2D(center, -angle, 1)
dst = cv2.warpAffine(image, rot_map, (w, h), cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("morph", morph)
cv2.imshow("line_detect", canny_line)
cv2.resizeWindow("line_detect", 250, canny_line.shape[0])
cv2.imshow("dst", dst)
cv2.waitKey(0)