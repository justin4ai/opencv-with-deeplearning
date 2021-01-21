import numpy as np, cv2

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = image[y1:y2, x1:x2].astype('float32')
            tmp = cv2.multiply(roi, mask)
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst

image = cv2.imread("images/Q10.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

R, G, B = cv2.split(image)

mask_blur = np.array([ 1/9, 1/9, 1/9,
                  1/9, 1/9, 1/9,
                  1/9, 1/9, 1/9 ], np.float32).reshape(3, 3)

mask_sharpen = np.array([ 0, -1, 0,
                     -1,  5, -1,
                     0, -1, 0 ], np.float32).reshape(3, 3)
#mask_sharpen = np.array([ -1, -1, -1,
#                     -1,  9, -1,
#                     -1, -1, -1 ], np.float32).reshape(3, 3)

avg_blur_R = filter(R, mask_blur).astype('uint8')
avg_blur_G = filter(G, mask_blur).astype('uint8')
avg_blur_B = filter(B, mask_blur).astype('uint8')

sharpen_R = filter(R, mask_sharpen).astype('uint8')
sharpen_G = filter(G, mask_sharpen).astype('uint8')
sharpen_B = filter(B, mask_sharpen).astype('uint8')

bluring_User = cv2.merge([avg_blur_R, avg_blur_G, avg_blur_B])
bluring_User = cv2.convertScaleAbs(bluring_User)
sharpen_User = cv2.merge([sharpen_R, sharpen_G, sharpen_B])
Sharpen_User = cv2.convertScaleAbs(sharpen_User)

bluring_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_blur))
sharpen_OpenCV = cv2.convertScaleAbs(cv2.filter2D(image, cv2.CV_16S, mask_sharpen))

titles = ['image', 'bluring_User', 'bluring_OpenCV', 'sharpen_User', 'sharpen_OpenCV']
for t in titles:
    cv2.imshow(t, eval(t))
cv2.waitKey(0)