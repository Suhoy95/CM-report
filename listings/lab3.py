import numpy as np

ny = 1

y1_0 = 0.724197
y2_0 = 0

y1 = [y1_0]
y2 = [y2_0]
eps = 0.5 * 10 ** -4

# метод Эйлера с большей точностью
h = 0.0001
for i in range(100000):
    y1.append(y1[-1] + h*(y2[-1]))
    y2.append(y2[-1] +
                h * (-3*y2[-1] ** 3 + ny * y2[-1] - y1[-1]))
    # считаем цикл завершенным, когда покоординатно 
    # приблизились к начальной точке ближе, чем на eps
    if (np.abs(y1_0 - y1[-1]) < eps and
        np.abs(y2_0 - y2[-1]) < eps):
        print("h={h}, i={i}, h*i={period}".format(
              h=h, i=i+1, period=h*(i+1))
        )
        break
