import warnings
import cv2
import numpy as np
from Common.filters import filter

warnings.filterwarnings(action="ignore")

import tensorflow as tf

new_model = tf.keras.models.load_model('0220_alexnet.model')
# new_model = tf.keras.models.load_model('tmp8000.model')

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

data1 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]

mask1 = np.array(data1, np.float32)

image = []

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0 : break

    title = "View Frame from Camera"
    image = frame.copy()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # image = filter(image, mask1)
    # image = cv2.convertScaleAbs(image)
    cv2.imshow("B", image)

    image = cv2.resize(image,(227,227))
    image = image.reshape(1,227,227,1)

    predictions = new_model.predict(image)
    print(np.argmax(predictions[0]))

    '''frame = frame.reshape(227, 227, 3)'''

    if int(np.argmax(predictions[0])) == 0:
        cv2.putText(frame, 'true', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,2, 200)
    else:
        cv2.putText(frame, 'false', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 200)

    cv2.imshow(title, frame)