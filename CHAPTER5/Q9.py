import numpy as np, cv2

mat = np.full((600, 400, 3), (255, 255, 255), np.uint8)

title = 'Q9'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)


cv2.rectangle(img = mat, rec = (100, 100, 200, 300), color = (0, 0, 255), lineType = cv2.LINE_4, thickness = 10)

cv2.imshow(title, mat)
cv2.waitKey(0)
cv2.destroyAllWindows()