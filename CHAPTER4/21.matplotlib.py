import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/matplot.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

rows, cols = image.shape[:2]

rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # 컬러 공간변환
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 명암도 영상 변환

fig = plt.figure(num=1, figsize=(3,4))
plt.imshow(image), plt.title("figure1- original(bgr)")
plt.axis('off'), plt.tight_layout()

fig = plt.figure(figsize=(6,4))

plt.suptitle("figure2- pyplot image display")
plt.subplot(1,2,1), plt.imshow(rgb_img) ## 1행 2열 중 첫 번째
plt.axis([0, cols, rows, 0]), plt.title('rgb color')
plt.subplot(1,2,2), plt.imshow(gray_img, cmap='gray')
plt.title("gray_img2")
plt.show()
