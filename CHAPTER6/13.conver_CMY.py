import numpy as np, cv2

BGR_img = cv2.imread("images/color_model.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
CMY_img = white - BGR_img
Yellow, Magenta, Cyan = cv2.split(CMY_img)

titles = ['BGR_img', 'CMY_img', 'Yellow', 'Magenta', 'Cyan']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)