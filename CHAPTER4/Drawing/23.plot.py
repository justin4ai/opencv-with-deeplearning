import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = np.arange(10)
y2 = np.arange(10)**2
y3 = np.random.choice(50, size=10)

plt.figure(figsize = (5,3))
plt.plot(x, y1, 'b--', linewidth=2)
plt.plot(x, y2, 'go-', linewidth=3)
plt.plot(x, y3, 'c+:', linewidth=5)

plt.title('Line examples')
plt.axis([0, 10, 0, 80])
plt.tight_layout()
plt.savefig(fname='sample.png', dpi=300) ## 그림 저장
plt.show()
