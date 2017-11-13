import numpy as np

ny = 1     # Параметр системы
h = 0.0001 # шаг метода Эйлера
           # и основание прямоугольников при интегрировании


def line(y1_0, y2_0):
    """
    Вычисление системы методом Эйлера от точки (y1_0, y2_0)
    за счет правильно подобраных в предыдущей работе координат
    функция вычислит близкую к предельному циклу траекторию
    """
    y1 = [y1_0]
    y2 = [y2_0]
    eps = 0.5 * 10 ** -4
    for i in range(100000):
        y1.append(y1[i] + h * (y2[i]))
        y2.append(y2[i] +
                  h*(-3*y2[i] ** 3 + ny * y2[i] - y1[i]))
        if (np.abs(y1_0 - y1[i + 1]) < eps and
            np.abs(y2_0 - y2[i + 1]) < eps):
            return (y1, y2)

    raise Exception("Cycle not found")


def integral_from_div(cycle_y1, cycle_y2):
    """
    Вычисление интеграла от дивергенции системы
    вдоль цикла
    """
    sum = 0
    for j in range(len(cycle_y1)):
        sum += -9 * cycle_y2[j] ** 2 + ny
    sum *= h
    return sum

# Основная программа
cycle_y1, cycle_y2 = line(0.72424, 0)
s = integral_from_div(cycle_y1, cycle_y2)
print("Integral of the divergence: {}".format(s))
