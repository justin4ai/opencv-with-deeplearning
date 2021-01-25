import numpy as np, cv2

image = cv2.imread("images/Q17.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

h, w = image.shape

print(h)
print(w)

flip1 = np.float32([[-1,0,563],[0,1,0]])
flip2 = np.float32([[1,0,1],[0,-1,447]])
flip3 = np.float32([[-1,0,563],[0,-1,447]])

dst1 = cv2.warpAffine(image, flip1, (w,h))
dst2 = cv2.warpAffine(image, flip2, (w,h))
dst3 = cv2.warpAffine(image, flip3, (w,h))

# cv2.namedWindow('flip1', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', image);     cv2.imshow('flip1', dst1)
# cv2.resizeWindow('flip1', 800, 800)
cv2.imshow('flip2', dst2);      cv2.imshow('flip3', dst3)
cv2.waitKey(0)