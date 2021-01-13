import numpy as np, cv2

def onChangeR(pos):
    global radius
    radius = pos

def onChangeB(pos):
    global bold
    bold = pos


def onMouse(event, x, y, flags, param):
    global title, mat, radius, bold
    if event == cv2.EVENT_RBUTTONDOWN:
        # 원
        cv2.circle(mat, (x, y), radius, (0, 0, 255), bold)
        cv2.imshow(title, mat)

    elif event == cv2.EVENT_LBUTTONDOWN:
        # 사각형
        cv2.rectangle(mat, (x, y, 30, 30), (0, 255, 0), bold, cv2.LINE_4)
        cv2.imshow(title, mat)


radius = 20
bold = 1

mat = np.full((600, 900, 3), (255, 255, 255), np.uint8)

print(mat)

title = 'Q10'
bar_name_rad = 'Radius'
bar_name_bold = 'Thickness'

cv2.imshow(title, mat)
cv2.setMouseCallback(title, onMouse)

cv2.createTrackbar(bar_name_rad, title, radius, 50, onChangeR)
cv2.createTrackbar(bar_name_bold, title, bold, 10, onChangeB)

cv2.waitKey(0)
#cv2.destroyAllWindows()