import numpy as np, cv2

def calc_histo(image, histSize, ranges=[0, 256]):
    hist = np.zeros((histSize, 1), np.float32)
    gap = ranges[1] / histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1
    return hist

image = cv2.imread("images/Q14.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 실패")

HSV_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
Hue, Saturation, Intensity = cv2.split(HSV_img)



#dst = np.zeros(image.shape[:2], np.uint8)
#hue = calc_histo(Hue, dst.shape[0])
#saturation = calc_histo(Saturation, dst.shape[1])

histo = cv2.calcHist( [HSV_img], [0, 1], None, [180, 256], [0, 180, 0, 256] )
#histo = histo.astype(np.uint8)

dst = np.full((180, 256), 255, np.uint8)
'''for i in range(dst.shape[0]):
    for j in range(dst.shape[1]):
        dst.itemset((i, j), )'''

new_hue = np.array([ [ 179-j for i in range(256)] for j in range(180)])
new_hue = new_hue.astype(np.float32)
new_saturation = np.array([ [j for j in range(256) ] for i in range(180)])
new_saturation = new_saturation.astype(np.float32)


#print(type((histo/max(histo.flatten()))[0][0]))
dst = cv2.merge([new_hue, new_saturation, histo/10])
#dst = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)


print(new_hue)

title1 = "image"
title2 = "dst"

cv2.namedWindow(title1, cv2.WINDOW_NORMAL)
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.resizeWindow(title1, 600, 400)
cv2.resizeWindow(title2, 600, 400)

cv2.imshow(title1, image)
cv2.imshow(title2, cv2.convertScaleAbs(dst))

cv2.waitKey(0)