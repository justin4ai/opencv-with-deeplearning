import cv2
import random
import pickle, getpass
import numpy as np

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

cnt = 0

x_train_color = []
x_test_color = []

x_train_gray = []
x_test_gray = []

image = []
color_data = []
color_data2 = []
gray_data = []
gray_data2 = []

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0 : continue

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    title = "View Frame from Camera"

    if cnt % 4 == 0:
        '''cv2.imwrite(f"images/{int(cnt)}.jpg", frame)'''
        image = frame
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                 # 프레임 받아서 grayscale로 전환

        color_data.append(frame)
        gray_data.append(image)
    cnt += 1
    cv2.imshow(title, frame)

    if cnt == 5000: break

color_data2 = [random.choice(color_data) for i in range(1250)]
x_train_color = color_data2[:1000]
x_test_color = color_data2[1000:1251]

gray_data2 = [random.choice(gray_data) for i in range(1250)]
x_train_gray = gray_data2[:1000]
x_test_gray = gray_data2[1000:1251]

# train data pickle

pickle_out = open(f"{getpass.getuser()}_x_train_color_F.pickle", "wb")
pickle.dump(x_train_color, pickle_out)
pickle_out.close()

pickle_out = open(f"{getpass.getuser()}_x_train_gray_F.pickle", "wb")
pickle.dump(x_train_gray, pickle_out)
pickle_out.close()

# test data pickle

pickle_out = open(f"{getpass.getuser()}_x_test_color_F.pickle", "wb")
pickle.dump(x_test_color, pickle_out)
pickle_out.close()

pickle_out = open(f"{getpass.getuser()}_x_test_gray_F.pickle", "wb")
pickle.dump(x_test_gray, pickle_out)
pickle_out.close()

capture.release()