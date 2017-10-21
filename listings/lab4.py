import numpy as np

ny = 1     # Параметр системы
h = 0.0001 # Общий шаг метода Эйлера

def line(y1_0, y2_0):
    """
    Вычисление системы методом Эйлера от точки (y1_0, y2_0)
    за счет правильно подобраных в прошлой работе координат
    функция вычислит близкую к предельному циклу траекторию
    """
    y1 = [y1_0]
    y2 = [y2_0]
    eps = 0.5 * 10 ** -4
    for i in range(100000):
        y1.append(y1[-1] + h * y2[-1])
        y2.append(y2[-1] +
                  h*(-3*y2[-1] ** 3 + ny * y2[-1] - y1[-1]))
        if (np.abs(y1_0 - y1[-1]) < eps and
            np.abs(y2_0 - y2[-1]) < eps):
            return (y1, y2)

    raise Exception("Cycle not found")

def linear_form(y1_0, y2_0, cycle_y1, cycle_y2):
    """
    Решение линеаризованной системы вдоль цикла
    """
    y1 = [y1_0]
    y2 = [y2_0]
    for j in range(len(cycle_y1)):
        y1.append(y1[-1] + h * (y2[-1]))
        y2.append(y2[-1] + h * (-y1[-1] +
                       (-9*cycle_y2[j] ** 2 + ny) * y2[-1]))
    return [y1[-1], y2[-1]]

# Начало программы
# вычисление поточечного описания предельного цикла
cycle_y1, cycle_y2 = line(0.724197, 0)

# решение линеаризированной системы
# с начальными условиями (1, 0) и (0, 1)
f1 = linear_form(1, 0, cycle_y1, cycle_y2)
f2 = linear_form(0, 1, cycle_y1, cycle_y2)

# Матрица монодромии
f = np.array([
    [f1[0], f2[0]],
    [f1[1], f2[1]],
])
print("F-matrix:")
print(f)

# Вычисление собственных чисел матрицы монодромии
p = np.linalg.eig(f)
print("Eigenvalues:")
print(p[0])
