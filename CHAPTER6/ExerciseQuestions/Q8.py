import cv2
import numpy as np

image1 = cv2.imread("images/Q8_1.jpg", cv2.IMREAD_GRAYSCALE)[:300, :300]
image2 = cv2.imread("images/Q8_2.jpg", cv2.IMREAD_GRAYSCALE)[:300, :300]
image3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

dst = np.concatenate([image1, image3, image2], axis = 1)

title = "dst"
cv2.imshow(title, dst)
cv2.waitKey(0)