import cv2
from Common.utils import put_string

def zoom_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value):
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

def brightness_bar(pos):
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, pos)

def contrast_bar(pos):
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, pos)

capture = cv2.VideoCapture(0)
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)


title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar)
cv2.createTrackbar('focus', title, 0, 40, focus_bar)
cv2.createTrackbar('brightness', title, 0, 100, brightness_bar)
cv2.createTrackbar('contrast', title, 0, 100, contrast_bar)

while True:
    ret, frame = capture.read() # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break
    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    brightness = int(capture.get(cv2.CAP_PROP_BRIGHTNESS))
    contrast = int(capture.get(cv2.CAP_PROP_CONTRAST))
    put_string(frame, 'zoom : ', (10 , 240), zoom)  # 줌 값 표시
    put_string(frame, 'focus : ', (10, 270), focus) # 초점 값 표시
    put_string(frame, 'brightness : ', (10, 300), brightness)  # 줌 값 표시
    put_string(frame, 'contrast : ', (10, 330), contrast)  # 초점 값 표시
    cv2.imshow(title, frame)

capture.release()
