import numpy as np, cv2

def draw_points(image, group, color):
    for p in group:
        pt = tuple(p.astype(int))       # 정수 원소 튜플
        cv2.circle(image, pt, 3, color, cv2.FILLED)

nsample = 50        # 그룹당 학습 데이터 수
traindata = np.zeros((nsample * 2, 2), np.float32)      # 전체 학습 데이터 행렬
label = np.zeros((nsample * 2, 1), np.float32)      # 레이블 행렬 생성

cv2.randn(traindata[:nsample], 150, 30)     # 정규분포 랜덤 값 생성
cv2.randn(traindata[nsample:], 250, 60)
label[:nsample], label[nsample:] = 0, 1     # 레이블 기준값 지정

K = 7
knn = cv2.ml.KNearest_create()      # kNN 클래스로 객체 생성
knn.train(traindata, cv2.ml.ROW_SAMPLE, label)     # 학습 수행

points = [(x, y) for y in range(400) for x in range(400)]       # 검사 좌표 리스트 생성
ret, resp, neig, dist = knn.findNearest(np.array(points, np.float32), K)        # 분류수행

colors = [(0, 180, 0) if p else (0, 0, 180) for p in resp]
image = np.reshape(colors, (400, 400, 3)).astype('uint8')       # 3채널 컬러

draw_points(image, traindata[:nsample], color = (0, 0, 255))
draw_points(image, traindata[nsample:], color = (0, 255, 0))
cv2.imshow("sample K=" + str(K), image)
cv2.waitKey(0)