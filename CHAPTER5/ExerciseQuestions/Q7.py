import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)  # (517, 585, 3)
if logo is None : raise Exception("영상파일 읽기 오류")

print(logo.shape)

blue, green, red = cv2.split(logo)

# 빈 채널
b_zeros, g_zeros, r_zeros = np.zeros((517, 585), np.uint8), np.zeros((517, 585), np.uint8), np.zeros((517, 585), np.uint8)

# 채널 합성
blue_img = cv2.merge([blue, g_zeros, r_zeros])
green_img = cv2.merge([b_zeros, green, r_zeros])
red_img = cv2.merge([b_zeros, g_zeros, red])

cv2.imshow("logo", logo)
cv2.imshow("blue_img", blue_img)
cv2.imshow("green_img", green_img)
cv2.imshow("red_img", red_img)
cv2.waitKey(0)