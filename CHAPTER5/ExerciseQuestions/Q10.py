import cv2
import numpy as np

def put_string(frame, text, pt, value, color=(120, 200, 90) ):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

## 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

_, tmp = capture.read()
mask = np.zeros(tmp.shape[:2], np.uint8)
mask[:200,:100] = 255

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    mask_sum = cv2.sumElems(frame[mask!=0])
    mask_mean = cv2.mean(frame, mask)

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_string(frame, 'EXPOS', (10, 40), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)
    print("[관심 영역 합] :{}".format(mask_sum))
    print("[관심 영역 평균] :{}".format(mask_mean))

capture.release()
