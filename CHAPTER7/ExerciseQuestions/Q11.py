import numpy as np, cv2

def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter, j + v - xcenter
                    sum += image[y, x] * mask[u, v]

            dst[i, j] = sum
    return dst

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter2(image, mask1)
    dst2 = filter2(image, mask2)
    dst1, dst2 = np.abs(dst1), np.abs(dst2)
    dst = cv2.magnitude(dst1, dst2)

    dst = np.clip(dst, 0, 255).astype('uint8')
    dst1 = np.clip(dst1, 0, 255).astype('uint8')
    dst2 = np.clip(dst2, 0, 255).astype('uint8')

    return dst, dst1, dst2

image = cv2.imread("images/Q11.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 실패")

data_roberts_1 = [ -1, 0, 0,
                    0, 1, 0,
                    0, 0, 0 ]
data_roberts_2 = [ 0, 0, -1,
                   0, 1,  0,
                   0, 0,  0 ]

data_prewitt_1 = [ -1, 0, 1,
                   -1, 0, 1,
                   -1, 0, 1 ]
data_prewitt_2 = [ -1, -1, -1,
                    0,  0,  0,
                    1,  1,  1 ]

data_sobel_1 = [ -1, 0, 1,
                 -2, 0, 2,
                 -1, 0, 1 ]
data_sobel_2 = [ -1, -2, -1,
                  0,  0,  0,
                  1,  2,  1 ]

Roberts, _, __ = differential(image, data_roberts_1, data_roberts_2)
print(Roberts)
Prewitt = differential(image, data_prewitt_1, data_prewitt_2)[0]
Sobel = differential(image, data_sobel_1, data_sobel_2)[0]

titles = ['Roberts', 'Prewitt', 'Sobel']
for t in titles:
    cv2.imshow(t, eval(t))
cv2.waitKey(0)