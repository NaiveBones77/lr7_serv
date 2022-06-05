import numpy as np


def checkS(message, dictK:dict):
    a = message.replace(",", ".").split(" ")
    x = float(a[0]) / 1000
    h = float(a[1]) / 1000
    y = float(a[2]) / 1000
    key = a[3]
    num = a[3]

    dictK.update({key: [x, y, h, num]})

    return dictK

def formList(dictK:dict):
    x = []
    y = []
    h = []
    num = []
    lst = list(dictK.values())
    for items in lst:
        x.append(items[0])
        y.append(items[1])
        h.append(items[2])
        num.append(items[3])

    return (x, y, h, num)

def from_start2img(h, w, x, y):
    h_new = []
    w_new = []

    for i in range(len(y)):
        if y[i] == 0:
            y_new = 20000
        elif y[i] < 0:
            y_new = 20000 - 1000 * abs(y[i])
        elif y[i] > 0:
            y_new = 1000 * y[i] + 20000

        w_new.append(y_new / 40000 * w)

    for i in range(len(x)):
        if x[i] == 0:
            x_new = 20000
        elif x[i] > 0:
            x_new = 1000 * x[i] + 20000
        elif x[i] < 0:
            x_new = 20000 - 1000 * abs(x[i])

        h_new.append(x_new / 40000 * h)

    return (h_new, w_new)