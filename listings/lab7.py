# Лаб. работа 7: влияние переменного запаздывания на систему
import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


figure, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
# подпись осей на графике
ax.set_xlabel("y1")
ax.set_ylabel("y2")


ny = 1
alpha0 = 0.01

N = 100
tao = 3
h = tao / N
T = 200

def line(y1_0, y2_0, alpha):
    # решение задачи методом Эйлера
    y1 = copy.deepcopy(y1_0)
    y2 = copy.deepcopy(y2_0)
    for i in range(len(y1_0)-1, int(T / h)):
        # Запаздывание влияет на y1
        # y1.append(y1[i] + h * (y2[i] +
        #                        alpha * y1[i - int(N * np.sin(2*i*h/T))]))
        # y2.append(y2[i] +
        #           h * (-3*y2[i] ** 3 + ny * y2[i] - y1[i]))

        # Запаздывание влияет на y2
        y1.append(y1[i] + h * (y2[i]))
        y2.append(y2[i] +
                  h * (-3*y2[i] ** 3 + ny * y2[i] - y1[i] +
                       alpha * y1[i - int(N * np.sin(2*i*h/T))]))
    ax.plot(y1, y2)


def update_plot(strAlpha):
    # перерисовка графика в зависимости от параметра
    alpha = float(strAlpha)
    ax.cla()
    line(
        [0.1 for a in range(N)],
        [0.1 for a in range(N)],
        alpha)
    line(
        [2 for a in range(N)],
        [2 for a in range(N)],
        alpha)
    figure.canvas.draw_idle()


axfreq = plt.axes([0.13, 0.05, 0.55, 0.03])
textBox = TextBox(axfreq, 'alpha', initial=str(alpha0))
textBox.on_submit(update_plot)

def _keyboard_handler(event):
    # выход при нажатии escape
    if event.key == 'escape':
        plt.close('all')


figure.canvas.mpl_connect('key_press_event', _keyboard_handler)

update_plot(alpha0)
plt.show()
