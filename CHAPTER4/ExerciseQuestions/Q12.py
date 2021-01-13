import numpy as np
import cv2

switch_case = {
    2424832 : "왼쪽",
    2555904 : "오른쪽"
}

def onChange(value):
    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image = image + add_value
    cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break

    try:
        if switch_case[key] == "왼쪽":
            if (image[0][0] >= 10): image = image - 10
            cv2.setTrackbarPos('Brightness', title, image[0][0])
            cv2.imshow(title, image)
        elif switch_case[key] == "오른쪽":
            if (image[0][0] < 246): image = image + 10
            cv2.setTrackbarPos('Brightness', title, image[0][0])
            cv2.imshow(title, image)

    except KeyError:
        result = -1

cv2.destroyAllWindows()