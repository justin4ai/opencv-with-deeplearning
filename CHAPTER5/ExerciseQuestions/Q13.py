import numpy as np, cv2

image = np.zeros((400, 600), np.uint8)

x = np.array([np.random.randint(100, 500) for i in range(10)])
y = np.array([np.random.randint(50, 250) for i in range(10)])
w = np.array([np.random.randint(50, 100) for i in range(10)])
h = np.array([np.random.randint(100, 150) for i in range(10)])
c = np.array([np.random.randint(50, 255) for i in range(10)])
a = w * h

array = np.array([cv2.rectangle(image, tuple([x[i], y[i],
                                              w[i], h[i]]),
                                              np.random.randint(50,255), 4, cv2.LINE_4) for i in range(10)])

for i in range(len(x)):
    cv2.putText(image, '{}'.format(i+1), (x[i], y[i]), cv2.FONT_HERSHEY_SIMPLEX, 1, int(c[i]), 3)

idx = cv2.sortIdx(a, cv2.SORT_EVERY_COLUMN)
print(array[idx.astype('int')])


title = 'Q13'
cv2.imshow(title, image)
cv2.waitKey(0)

print(cv2.sumElems(array[idx.astype('int')][0]))