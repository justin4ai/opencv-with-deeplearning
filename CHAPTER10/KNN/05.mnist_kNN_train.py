import cv2, numpy as np
import pickle, gzip, os
from urllib.request import urlretrieve      # 웹사이트 링크 다운로드 함수
import matplotlib.pyplot as plt

def load_mnist(filename):       # mnist 데이터셋 다운로드 함수
    if not os.path.exists(filename):        # 현재 폴더에 파일 없으면 다운
        print("downlodaing")
        link = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
        # link = "http://deeplearning.net/data/mnist/mnist.pkl.gz"
        urlretrieve(link, filename)        # 다운로드
    #with gzip.open(filename, 'rb') as f:
        #f = pickle._Unpickler(f)
        #return pickle.load(f, encoding = "latin1")  # pickle 모듈로 파일에서 로두함
    with gzip.open('mnist.pkl.gz', 'rb') as f:
        data = pickle._Unpickler(f)
        data.encoding = 'latin1'  # set encoding
        return data.load()


def graph_image(data, label, title, nsample):       # 데이터 시각화 함수
    plt.figure(num = title, figsize = (10, 10))
    rand_idx = np.random.choice(range(data.shape[0]), nsample)      # 데이터 번호 랜덤 생성
    for i, id in enumerate(rand_idx):
        img = data[id].reshape(28, 28)      # 1행 행렬을 영상 형태로 변경
        plt.subplot(6, 4, i + 1), plt.axis('off'), plt.show(img, cmap = 'gray')
        plt.title("%s: %d" % (title, label[id]))        # 서브플롯 타이틀
        plt.tight_layout

train_set, valid_set, test_set = load_mnist("mnist.pkl.gz") # mnist 데이터셋 다운

## mnist 로드 데이터 크기 확인
print("train_set=", train_set[0].shape)     # 학습 데이터셋
print("valid_set=", train_set[0].shape)     # 검증 데이터셋
print("test_set=", test_set[0].shape)       # 테스트 데이터셋

print("training...")
knn = cv2.ml.KNearest_create()
knn.train(train_data, cv2.ml.ROW_SAMPLE, train_label)       # k-NN 학습 수행

nsample = 100
print("%d 개 predicting..." % nsample)
_, resp, _, _ = knn.findNearest(test_data[:sample], k = 5)      # k-NN 분류 수행
accur = sum(resp.flatten() == test_label[:nsample])        # 분류 정확도 측정

print("정확도 = ", accur / nsample * 100, '%')
graph_image(train_data, train_label, 'label', 24)       # 데이터로 영상 그리기
graph_image(test_data[:nsample], resp, 'predict', 24)
plt.show()      # 2개 그림 동시에 열기