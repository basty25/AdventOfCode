import numpy as np

test = np.genfromtxt("day04/test04.txt", dtype=str, delimiter=1)
data = np.genfromtxt("day04/input04.txt", dtype=str, delimiter=1)

def adjacent(data, x, y):
    n = data.shape[0]
    count = -1 # say we are on a "@"
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0 or i >= n or j >= n:
                continue
            if data[i, j] == "@":
                count += 1
    return count


def first(data):
    data_copy = np.copy(data)
    count = 0
    n = data.shape[0]
    for i in range(n):
        for j in range(n):
            if data[i, j] == "@":
                adj = adjacent(data, i, j)
                if adj < 4:
                    count += 1
                    data_copy[i,j] = "."


    # print(data_copy)
    return count, data_copy

print(first(test)[0])
print(first(data)[0])


def second(data):
    count = 0
    while True:
        c, data = first(data)
        count += c
        if c == 0:
            break

    return count

print(second(test))
print(second(data))
