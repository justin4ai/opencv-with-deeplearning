import cv2
import numpy as np

image1 = cv2.imread("images/Q8_1.jpg", cv2.IMREAD_GRAYSCALE)[:300, :300]
image2 = cv2.imread("images/Q8_2.jpg", cv2.IMREAD_GRAYSCALE)[:300, :300]

def onAlpha(pos):
    global title, alpha
    alpha = pos
    image3 = cv2.addWeighted(image1, alpha / 100, image2, beta / 100, 0)
    dst = np.concatenate([image1, image3, image2], axis=1)
    cv2.imshow(title, dst)

def onBeta(pos):
    global title, beta
    beta = pos
    image3 = cv2.addWeighted(image1, alpha / 100, image2, beta / 100, 0)
    dst = np.concatenate([image1, image3, image2], axis=1)
    cv2.imshow(title, dst)

alpha, beta = 50, 50
image3 = cv2.addWeighted(image1, alpha/100, image2, beta/100, 0)
dst = np.concatenate([image1, image3, image2], axis = 1)

title = "dst"
bar_name1 = "Alpha"
bar_name2 = "Beta"
cv2.imshow(title, dst)

cv2.createTrackbar(bar_name1, title, alpha, 100, onAlpha)
cv2.createTrackbar(bar_name2, title, beta, 100, onBeta)
cv2.waitKey(0)
cv2.destroyAllWindows()