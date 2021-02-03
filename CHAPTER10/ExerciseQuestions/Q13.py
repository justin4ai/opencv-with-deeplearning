import numpy as np, cv2

def place_middle(number, new_size):
    h, w = number.shape[:2]
    frame = max(h, w)
    square = np.full((frame, frame), 255, np.float32)

    dx, dy = np.subtract(frame, (w, h)) // 2
    square[dy:dy + h, dx:dx + w] = number
    return cv2.resize(square, new_size).flatten()