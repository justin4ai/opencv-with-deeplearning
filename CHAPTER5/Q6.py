import numpy as np
import cv2

image = np.full((300, 400), 100, np.uint8)

title = 'Q6'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, image)
cv2.resizeWindow(title, (500, 600))
cv2.waitKey(0)
cv2.destroyAllWindows()