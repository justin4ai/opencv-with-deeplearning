import numpy as np, cv2

def morphology(img, filterType ,mask=None):
    dst = np.zeros(img.shape, np.uint8)
    if mask is None: np.ones((3, 3), np.uint8)
    ycenter, xcenter = np.divmod(mask.shape[:2], 2)[0]

    if filterType == 'erosion':
        a, mcnt, b = 255, cv2.countNonZero(mask), 0
    elif filterType == 'dilation' :
        a, mcnt, b = 0, 0, 255

    for i in range(ycenter, img.shape[0] - ycenter):
        for j in range(xcenter, img.shape[1] - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2]
            temp = cv2.bitwise_and(roi, mask)
            cnt = cv2.countNonZero(temp)  # 일치 원소 개수 계산
            dst[i, j] = a if (cnt == mcnt) else b
    return dst

