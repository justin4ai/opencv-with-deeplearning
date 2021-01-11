import numpy as np
import cv2, time
def print_matInfo(name, image):

    if image.dtype == 'uint8':  mat_type = "CV_8U"
    elif image.dtype == 'int8':  mat_type = "CV_8S"
    elif image.dtype == 'uint16':  mat_type = "CV_16U"
    elif image.dtype == 'int16':  mat_type = "CV_16S"
    elif image.dtype == 'float32':  mat_type = "CV_32F"
    elif image.dtype == 'float64':  mat_type = "CV_64F"
    nchannel = 3 if image.ndim == 3 else 1

    # depth, channel 출력
    print("%12s: depth(%s), channels(%s) -> mat_type(%sC%d)"
          % (name, image.dtype, nchannel, mat_type, nchannel))

def put_string(frame, text, pt, value, color=(120, 200, 90) ):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)
