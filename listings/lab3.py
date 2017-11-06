import numpy as np

ny = 1

y1_0 = 0.72424
y2_0 = 0

y1 = [y1_0]
y2 = [y2_0]
eps = 0.5 * 10 ** -4

# метод Эйлера с большей точностью
h = 0.0001
for i in range(100000):
    y1.append(y1[i] + h*(y2[i]))
    y2.append(y2[i] +
                h * (-3*y2[i] ** 3 + ny * y2[i] - y1[i]))
    # считаем цикл завершенным, когда покоординатно
    # приблизились к начальной точке ближе, чем на eps
    if (np.abs(y1_0 - y1[i+1]) < eps and
        np.abs(y2_0 - y2[i+1]) < eps):
        print("h={h}, i={i}, h*i={period}".format(
              h=h, i=i+1, period=h*(i+1))
        )
        break
