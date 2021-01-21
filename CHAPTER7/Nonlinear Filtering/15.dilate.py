import numpy as np, cv2

def dilate(img, mask):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: mask = np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)   # 중요 부분
            cnt = cv2.countNonZero(temp)    # 중요 부분
            dst[i, j] = 0 if (cnt == 0) else 255
    return dst

image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

mask = np.array([[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]]).astype('uint8')
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst1 = dilate(th_img, mask)
dst2 = cv2.dilate(th_img, mask)
# dst2 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask)

cv2.imshow("User dilate", dst1)
cv2.imshow("OpenCV dilate", dst2)
cv2.waitKey(0)