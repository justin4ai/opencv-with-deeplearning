import numpy as np, math
import matplotlib.pyplot as plt

def exp(knN):
    th = -2 * math.pi * knN     # 푸리에 변환 각도값
    return complex(math.cos(th), math.sin(th))  # 복소수 클래스

def dft(g):
    N = len(g)
    dst = [sum(g[n] * exp(k*n/N) for n in range(N)) for k in range(N) ]
    return np.array(dst)

def idft(g):
    N = len(g)
    dst = [sum(g[n] * exp(-k*n/N) for n in range(N)) for k in range(N)]

fmax = 1000 # 샘플링 주파수 1000Hz : 최대 주파수의 2배
dt = 1/fmax # 샘플링 간격
t = np.arange(0, 1, dt) # Time vector

g1 = np.sin(2 *np.pi * 50 * t)
g2 = np.sin(2 *np.pi * 120 * t)
g3 = np.sin(2 *np.pi * 260 * t)
g = g1 * 0.6 + g2 * 0.9 + g3 * 0.2

N = len(g)     # 신호 길이
df = fmax/N    # 샘플링 간격
f = np.arange(0, N, df)
xf = dft(g) * dt    # 저자구현 푸리에 변환 함수
g2 = idft(xf)

plt.figure(figsize = (10, 10))
plt.subplot(3, 1, 1), plt.plot(t[0:200], g[0:200]), plt.title("org signal")
plt.subplot(3, 1, 2), plt.plot(f, np.abs(xf) ), plt.title("dft amplitude")
plt.subplot(3, 1, 3), plt.plot(t[0:200], g[0:200]), plt.title("idft signal")
plt.show()