import time
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

fig, ax = plt.subplots()
th = np.linspace(0, 2*np.pi, 512)
ax.set_ylim(-1.5, 1.5)

ln, = ax.plot(th, np.sin(th))

def slow_loop(ln):

        ln.set_ydata(np.sin(((j // 10) % 5 * th)))
        ln.figure.canvas.draw_idle()

        ln.figure.canvas.flush_events()

slow_loop(ln, data)