# Лаб. работа 9: влияние случайной помехи на систему
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


figure, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)
# подпись осей на графике
ax.set_xlabel("y1")
ax.set_ylabel("y2")


ny = 1
sigma0 = 0

def line(y1_0, y2_0, sigma):
    # решение задачи методом Эйлера
    y1 = [y1_0]
    y2 = [y2_0]
    h = 0.03
    for i in range(20000):
        y1.append(y1[i] + h * (y2[i]) + np.sqrt(h) * sigma * np.random.randn())
        y2.append(y2[i] + h * (-3*y2[i] ** 3 + ny * y2[i] - y1[i]))
    ax.plot(y1, y2)


def update_plot(strSigma):
    # перерисовка графика в зависимости от параметра
    sigma = float(strSigma)
    ax.cla()
    _y = lambda a0: a0 + sigma * np.random.randn()
    line(_y(0.1), _y(0.1), sigma)
    line(_y(2), _y(2), sigma)
    figure.canvas.draw_idle()


axfreq = plt.axes([0.13, 0.05, 0.55, 0.03])
textBox = TextBox(axfreq, 'sigma', initial=str(sigma0))
textBox.on_submit(update_plot)

def _keyboard_handler(event):
    # выход при нажатии escape
    if event.key == 'escape':
        plt.close('all')


figure.canvas.mpl_connect('key_press_event', _keyboard_handler)

update_plot(sigma0)
plt.show()
