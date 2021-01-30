import numpy as np, cv2
from Common.utils import put_string

def cornerHarris(image, ksize, k):
    dx = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize)
    dy = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize)

    a = cv2.GaussianBlur(dx * dx, (5, 5,), 0)
    b = cv2.GaussianBlur(dy * dy, (5, 5), 0)
    c = cv2.GaussianBlur(dx * dy, (5, 5), 0)

    corner = (a * b - c**2) - k * (a + b)**2
    return corner

def drawCorner(corner, image, thresh):
    cnt = 0
    corner = cv2.normalize(corner, 0, 100, cv2.NORM_MINMAX)
    corners = []
    for i in range(1, corner.shape[0]-1):
        for j in range(1, corner.shape[1]-1):
            neighbor = corner[i-1:i+2, j-1:j+2].flatten()
            max = np.max(neighbor[1::2])
            if thresh < corner[i, j] > max: corners.append((j, i))

    for pt in corners:
        cv2.circle(image, pt, 3, (0, 230, 0), -1)
    print("임계값: %2d, 코너 계수: %2d" % (thresh, len(corners)))
    return image

def onCornerHarris(thresh):
    img1 = drawCorner(corner1, np.copy(image), thresh)
    img2 = drawCorner(corner2, np.copy(image), thresh)

    put_string(img1, "USER", (10, 30), "")
    put_string(img2, "OpenCV", (10, 30), "")
    dst = cv2.repeat(img1, 1, 2)
    dst[:, img1.shape[1]:, :] = img2
    cv2.imshow("harris detect", dst)

image = cv2.imread("images/harris.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

blocksize = 4
apertureSize = 3
k = 0.04
thresh = 2
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corner1 = cornerHarris(gray, apertureSize, k)
corner2 = cv2.cornerHarris(gray, blocksize, apertureSize, k)

onCornerHarris(thresh)
cv2.createTrackbar("Threshold", "harris detect", thresh, 20, onCornerHarris)
cv2.waitKey(0)