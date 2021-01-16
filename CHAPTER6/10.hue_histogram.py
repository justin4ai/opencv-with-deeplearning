import numpy as np, cv2

def make_palette(rows):
    ## 리스트 생성 방식
    hue = [round(i ** 180 / rows) for i in range(rows)]
    hsv = [[[h, 255, 255]] for h in hue]
    hsv = np.array(hsv, np.uint8)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def draw_hist_hue(hist, shape=(200, 256, 3)):
    hsv_palette = make_palette(hist.shape[0])
    hist_img = np.full(shape, 255,np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)

    gap = hist_img.shape[1] / hist.shape[0]
    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        color = tuple(map(int, hsv_palette[i][0]))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), color, cv2.FILLED)

    return cv2.flip(hist_img, 0)

image = cv2.imread("images/hue_hist.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue_hist = cv2.calcHist( [hsv_img], [0], None, [18], [0,180])
hue_hist_img = draw_hist_hue(hue_hist, (200, 360, 3))

cv2.imshow("image", image)
cv2.imshow("hue_hist_img", hue_hist_img)
cv2.waitKey(0)