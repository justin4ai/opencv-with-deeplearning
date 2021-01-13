import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_RBUTTONDOWN:
        # 원
        cv2.circle(mat, (x, y), 20, (0, 0, 255), 4)
        cv2.imshow(title, mat)

    elif event == cv2.EVENT_LBUTTONDOWN:
        # 사각형
        cv2.rectangle(mat, (x, y, 30, 30), (0, 255, 0), 4, cv2.LINE_4)
        cv2.imshow(title, mat)

mat = np.full((300, 300, 3), (255, 255, 255), np.uint8)

title = 'Q10'
cv2.imshow(title, mat)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
#cv2.destroyAllWindows()