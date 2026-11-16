import numpy as np
import matplotlib.pyplot as plt

test = np.loadtxt("day09/test09.txt", delimiter=",")
data = np.loadtxt("day09/input09.txt", delimiter=",")


def first(data):
    a, b = data[0], data[1]
    m = (abs(a[0] - b[0])+1) * (abs(a[1]-b[1])+1)
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            a, b = data[i], data[j]
            area = (abs(a[0] - b[0])+1) * (abs(a[1]-b[1]) + 1)
            if area > m:
                m = area
    return int(m)

print(first(test))
print(first(data))

def second(data):
    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes()
    ax.plot(data[:, 0], data[:, 1], "o")
    plt.show()
    ...

second(test)


