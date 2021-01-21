import numpy as np, cv2

switch_case = {
    2490368 : "위",
    2621440 : "아래"
}
no = 1
fname = "images/test_car/{0:02d}.jpg".format(no)
image = cv2.imread(fname, cv2.IMREAD_COLOR)
if image is None:
    print(str(no) + "번 영상파일이 없습니다.")

mask = np.ones((5, 17), np.uint8)   # 닫힘 연산 마스크
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray, (5, 5))   # 블러링
gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)  # 소벨 에지 검출

## 이진화 및 닫힘 연산 수행
th_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations = 3)

cv2.imshow("image", image)
cv2.imshow("binary image", th_img)
cv2.imshow("opening", morph)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        if switch_case[key] == "위":
            no += 1
        elif switch_case[key] == "아래":
            no -= 1

    except KeyError:
        result = -1


    fname = "images/test_car/{0:02d}.jpg".format(no)
    image = cv2.imread(fname, cv2.IMREAD_COLOR)
    if image is None:
        print(str(no) + "번 영상파일이 없습니다.")
        continue

    mask = np.ones((5, 17), np.uint8)   # 닫힘 연산 마스크
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))   # 블러링
    gray = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5)  # 소벨 에지 검출

    ## 이진화 및 닫힘 연산 수행
    th_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]
    morph = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations = 3)

    cv2.imshow("image", image)
    cv2.imshow("binary image", th_img)
    cv2.imshow("opening", morph)
