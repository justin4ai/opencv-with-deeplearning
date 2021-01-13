''' 원문
import numpy as np, cv2

image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (50, 130), (200, 300)

cv2.line(image, pt1, (100, 200))
cv2.line(image, pt2, (100, 100, 100))
cv2.rectangle(image, pt1, pt2, (255, 0, 255))
cv2.rectangle(image, pt1, pt2, (0, 0, 255))

title = "Line & Rectangle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import numpy as np, cv2

image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)

pt1, pt2 = (50, 130), (200, 300)

cv2.line(image, pt1, (100, 200), (150, 150, 150))   # color argument 추가
cv2.line(image, pt2, (100, 100), (150, 150, 150))   # second point argument 추가
cv2.rectangle(image, pt1, pt2, (255, 0, 255))
cv2.rectangle(image, pt1, pt2, (0, 0, 255))

title = "Line & Rectangle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

###############################################################################
###############################################################################
###############################################################################

''' 원문
import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    global title
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, pt, 5, 100, 1)    # img, center, radius, color, thickness
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, pt, pt+(30, 30), 100, 2)
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

import numpy as np, cv2

def onMouse(event, x, y, flags, param):
    pt = (100, 100)
    global image, title
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img = image, center = (x, y), radius = 5, color = 100, thickness = 1)    # img, center, radius, color, thickness
        cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img = image, rec = (x, y, 30, 30), color = 100 , thickness = 2, lineType = cv2.LINE_4)
        cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()