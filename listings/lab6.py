import matplotlib.pyplot as plt
import numpy as np

y1_01 = [1 for i in range(100)]
y2_01 = [1 for i in range(100)]

y1_02 = [1.5 for i in range(100)]
y2_02 = [1.5 for i in range(100)]

y1_03 = [2 for i in range(100)]
y2_03 = [2 for i in range(100)]

y1_04 = [2.5 for i in range(100)]
y2_04 = [2.5 for i in range(100)]


nu = 1
alpha = 1

def line(y1_0, y2_0, dy1, dy2):
    y1 = [y for y in y1_0]
    y2 = [y for y in y2_0]
    h = 0.01
    for i in range(200000):
        y1.append(y1[-1] + h*dy1(y1, y2))
        y2.append(y2[-1] + h*dy2(y1, y2))
    plt.plot(y1, y2)

dy1_1 = lambda y1, y2: y2[-1] + alpha * y2[-1 - 99];
dy2_1 = lambda y1, y2: -3*y2[-1] ** 3 + nu*y2[-1] - y1[-1] + alpha * y1[-1 - 99]

line(y1_01, y2_01, dy1_1, dy2_1)
line(y1_02, y2_02, dy1_1, dy2_1)
line(y1_03, y2_03, dy1_1, dy2_1)
line(y1_04, y2_04, dy1_1, dy2_1)

plt.show()
