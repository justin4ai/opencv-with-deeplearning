import cv2
import matplotlib.pyplot as plt


def get_cell(img, j, i, size):
    x, y = (j * size[0], i * size[1])
    return img[y:y + size[1], x:x + size[0]]


train_image = cv2.imread("images/train_numbers.png", cv2.IMREAD_COLOR)
if train_image is None: raise Exception("영상파일 읽기 에러")
train_image = train_image[5:405, 6:806]

size, K = (40, 40), 15
nclass, nsample = 10, 20
cells = [[get_cell(train_image, j, i, size) for j in range(nclass)] for i in range(nsample)]

for i, cell in enumerate(cells):
    plt.subplot(10, 20, i + 1), plt.axis('off'), plt.imshow(cell, cmap='gray')
plt.tight_layout(), plt.show()