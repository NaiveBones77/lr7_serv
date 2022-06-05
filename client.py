import socket
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # ADDED
from PIL import Image, ImageDraw # ADDED
import utils

localIP = "127.0.0.1"
localPort = 12346
bufferSize = 1024

dict1 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None}

plt.ion()

r = np.arange(0, 2, 0.01)
#fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection='polar')
ax2 = fig.add_subplot(1, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
img = plt.imread("map.png") # ADDED

plt.autoscale(False)
# Установить направление полярной оси
ax.set_theta_zero_location("N")
# задаем направление по часовой стрелке
ax.set_theta_direction(-1)
# отображение линии сетки полярного диаметра
ax.set_rticks([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) # Less radial ticks
ax.set_rlabel_position(-22.5) # Move radial labels away from plotted line
ax.grid(True)

ax2.set_xlim((0, 826))
ax2.set_ylim((0, 833))
ax2.imshow(img)

ax3.set_ylim((-0.1, 10))
ax3.set_xlim((-20, 20))
p2 = [0, 0.157]
p1 = [0.38786, 3.12315]
ax3.plot(p1, p2, 'g--')
p2 = [0, 0]
p1 = [0, 0.38786]
ax3.plot(p1, p2, 'g--')

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
# Listen for incoming datagrams

names = [1, 2, 3]
ann_list = []

while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    message = message.decode("utf-8")

    dict1 = utils.checkS(message, dict1)

    if (None in dict1.values()):
        pass
    else:
        x, y, h, num = utils.formList(dict1)

        scat = ax.scatter(np.arctan2(y, x), np.sqrt(np.power(x, 2) + np.power(y, 2)))

        for i, a in enumerate(ann_list):
            a.remove()
        ann_list[:] = []


        height, width = utils.from_start2img(833, 826, x, y)
        scat2 = ax2.scatter(width, height)
        scat3 = ax3.scatter(y, h)

        for i, txt in enumerate(num):
            ann1 = ax.annotate(num[i], (np.arctan2(y[i], x[i]), np.sqrt(np.power(x[i], 2)
                                                                         + np.power(y[i], 2))))
            ann2 = ax2.annotate(num[i], (width[i], height[i]))
            ann3 = ax3.annotate(num[i], (y[i], h[i]))

            ann_list.append(ann1)
            ann_list.append(ann2)
            ann_list.append(ann3)

        plt.draw()
        plt.pause(0.1)
        scat.remove()
        scat2.remove()
        scat3.remove()

        print(message)


