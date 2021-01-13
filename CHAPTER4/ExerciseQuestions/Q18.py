import numpy as np, cv2

image = np.full((400, 600, 3), (255, 255, 255), np.uint8)
center = (300, 200)
center_R = (350, 200)
center_L = (250,200)

cv2.ellipse(image, center, (100, 100), 180, 0, 180, (0, 0, 255), -1)
cv2.ellipse(image, center, (100, 100), 0, 0, 180, (255, 0, 0), -1)
cv2.ellipse(image, center_L, (50, 50), 0, 0, 180, (0, 0, 255), -1)
cv2.ellipse(image, center_R, (50, 50), 180, 0, 180, (255, 0, 0), -1)

title = "Q18"
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()