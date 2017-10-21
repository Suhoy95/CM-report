import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

ny0 = 0 # Первоначальное значения параметра

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.15)

# подпись осей на графике
ax.set_xlabel("y1")
ax.set_ylabel("y2")

# функция построение кривой методом Эйлера
def line(y1_0, y2_0, ny):
    y1 = [y1_0]
    y2 = [y2_0]
    h = 0.003
    for i in range(50000):
        y1.append(y1[-1] + h * (y2[-1]))
        y2.append(y2[-1] + 
                h * (-3*y2[-1] ** 3 + ny * y2[-1] - y1[-1]))
    ax.plot(y1, y2)

def streamplot(ny):
    # увеличиваем параметры сетки в зависимости от модуля ny
    b = (4 + np.abs(ny)) # границы сетки
    c = (100 + np.abs(ny)) * 1j # число точек разбиения
    Y, X = np.mgrid[-b:b:c, -b:b:c]
    Y1 = Y
    Y2 = -3 * Y ** 3 + ny * Y - X
    ax.streamplot(X, Y, Y1, Y2)

# перерисовка графика в зависимости от параметра
# выводится фазовый портрет и две линии
def update_plot(ny):
    ax.cla()
    streamplot(ny)
    line(1. / (np.abs(ny) + 1), 1. / (np.abs(ny) + 1), ny)
    line(-ny, -6, ny)
    fig.canvas.draw_idle()

# Слайдер - чтобы менять параметр без перезапуска программы
axfreq = plt.axes([0.13, 0.05, 0.55, 0.03])
slider = Slider(axfreq, 'Ny', -10.0, 20.0, valinit=ny0)
slider.on_changed(update_plot)

step = 0.1 # шаг изменения параметра по нажатии клавиши
def _keyboard_handler(event):
    # выход при нажатии escape
    if event.key == 'escape':
        plt.close('all')
    # уменьшение параметра при нажатии стрелки "вниз"
    elif event.key == 'down':
        slider.set_val(slider.val - step)
    # увелечение параметра при нажатии стрелки "вверх"
    elif event.key == 'up':
        slider.set_val(slider.val + step)

fig.canvas.mpl_connect('key_press_event', _keyboard_handler)

update_plot(ny0)
plt.show()
