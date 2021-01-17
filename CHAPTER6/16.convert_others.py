import cv2

BGR_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR)
if BGR_img is None: raise Exception("영상파일 읽기 오류")

Gray_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2GRAY)
YCC_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YCrCb)
YUV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2YUV)
LAB_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2LAB)

YCC_ch = cv2.split(YCC_img)
YUV_ch = cv2.split(YUV_img)
Lab_ch = cv2.split(LAB_img)

cv2.imshow("BGR_img", BGR_img)
cv2.imshow("Gray_img", Gray_img)

sp1, sp2, sp3 = ['Y', 'Cr', 'Cb'], ['Y', 'U', 'V'], ['L', 'A', 'B']
for i in range(3):
    cv2.imshow("YCC_img[%d]-%s" %(i, sp1[i]), YCC_ch[i])
    cv2.imshow("YUV_img[%d]-%s" % (i, sp2[i]), YUV_ch[i])
    cv2.imshow("LAB_img[%d]-%s" % (i, sp3[i]), Lab_ch[i])
cv2.waitKey(0)