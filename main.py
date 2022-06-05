import numpy as np
import time
import matplotlib.pyplot as plt
import random

# возвращает массив, содержащий равномерно расположенные значения внутри заданного интервала
# (начало, конец, шаг)
r = np.arange(0, 2, 0.01)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
#plt.ion()
# Установить направление полярной оси
ax.set_theta_zero_location("N")
# задаем направление по часовой стрелке
ax.set_theta_direction(-1)
# отображение линии сетки полярного диаметра
ax.set_rticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]) # Less radial ticks
ax.set_rlabel_position(-22.5) # Move radial labels away from plotted line

ax.grid(True)

mass1 = np.random.randint(1, 80, 50)
mass2 = np.random.randint(1, 80, 50)
mass = list(zip(mass1, mass2))
plt.title("Scatter Plot")



for point in mass:
    scat = plt.scatter(*point)
    plt.draw()
    plt.pause(2)
    scat.remove()

#ax.set_title("A line plot on a polar axis", va='bottom')
#plt.show()

