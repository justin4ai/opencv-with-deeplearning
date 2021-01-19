import numpy as np, cv2

image_original = cv2.imread("images/Q13.jpg", cv2.IMREAD_COLOR)

R, G, B = cv2.split(image_original)

Y = 0.299 * R + 0.587 * G + 0.114 * B
Cb = (R - Y) * 0.564 + 128
Cr = (B - Y) * 0.713 + 128

YCbCr = cv2.merge([Y, Cb, Cr])
Y, Cb, Cr = cv2.split(YCbCr)

R = Y + 1.403 * (Cr - 128)
G = Y - 0.714 * (Cr - 128) - 0.344 * (Cb - 128)
B = Y + 1.773 * (Cb - 128)

image_revised = cv2.merge([B, G, R])

title1 = 'Q13_original'
title2 = "Q13_revised"
cv2.imshow(title1, image_original)
cv2.imshow(title2, cv2.convertScaleAbs(image_revised))
cv2.waitKey(0)