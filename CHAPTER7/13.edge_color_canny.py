import cv2

def onTrackbar(th):
    rep_edge = cv2.GaussianBlur(rep_gray, (5, 5), 0)
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5)
    h, w = image.shape[:2]
    cv2.rectangle(rep_edge, (0, 0, w, h), 255, -1)
    color_edge = cv2.bitwise_and(rep_image, rep_image, mask=rep_edge)
    cv2.imshow("color edge", color_edge)

image = cv2.imread("images/color_edge.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

th = 50
rep_image = cv2.repeat(image, 1, 2)
rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar)
onTrackbar(th)
cv2.waitKey(0)