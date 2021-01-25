import numpy as np, cv2

def draw_bar(img, pt, w, bars):
    pt = np.array(pt, np.int)
    for bar in bars:
        (x, y), h = pt, w*6
        cv2.rectangle(img, (x, y, w, h), (0, 0, 0), -1)
        if bar == 0:
            y = int(y + 2.4 * w)
            h = int(w * 1)
            cv2.rectangle(img, (x, y, w, h), (255, 255, 255), -1)
        pt += (int(w*1.5), 0)


image = np.full((400, 600, 3), (255, 255, 255), np.uint8)
center = (300, 200)
center_R = (350, 200)
center_L = (250,200)

cv2.ellipse(image, center, (100, 100), 180, 0, 180, (0, 0, 255), -1)
cv2.ellipse(image, center, (100, 100), 0, 0, 180, (255, 0, 0), -1)
cv2.ellipse(image, center_L, (50, 50), 0, 0, 180, (0, 0, 255), -1)
cv2.ellipse(image, center_R, (50, 50), 180, 0, 180, (255, 0, 0), -1)

draw_bar(image, [65, 145], 15, [1, 1, 1])
draw_bar(image, [480, 145], 15, [0, 0, 0])


title = "Q18"
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()