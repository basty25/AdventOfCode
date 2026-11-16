import numpy as np

lines = np.loadtxt("day01/input01.txt", dtype=str)
test = np.loadtxt("day01/test01.txt", dtype=str)

def first():
    value = 50
    count = 0
    # for rotation in test:
    for rotation in lines:
        amount = int(rotation[1:])

        if rotation[0] == "L":
            value = (value - amount) % 100
        else:
            value = (value + amount) % 100
        if value == 0:
            count +=1
    return count

print(first())

def second():
    value = 50
    count = 0
    # for rotation in test:
    for rotation in lines:
        amount = int(rotation[1:])

        # multiple rotations
        if amount > 100:
            count += amount // 100
            amount = amount % 100

        # left rotation
        if rotation[0] == "L":
            if value - amount <= 0 and value != 0:
                count+=1
            value = (value - amount) % 100

        # right rotation
        else:
            if value + amount >= 100 and value != 0:
                count+=1
            value = (value + amount) % 100
    return count

print(second())