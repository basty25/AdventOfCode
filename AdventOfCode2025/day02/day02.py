import numpy as np

data = np.loadtxt("day02/input02.txt", delimiter=",", dtype=str)
test = np.loadtxt("day02/test02.txt", delimiter=",", dtype=str)

def first(data):
    count = 0
    for seq in data:
        start, end = map(int, seq.split("-"))
        for num in range(start, end+1):

            # prepare sequence
            num_str = str(num)
            l = len(num_str)
            if l % 2 == 1:
                continue

            # split and compare
            mid = int(l/2)
            a = int(num_str[:mid])
            b = int(num_str[mid:])
            if a == b:
                count += num

    return count

def check(arr: list):
    return arr.count(arr[0]) == len(arr)

def second(data):
    count = 0
    for seq in data:
        start, end = map(int, seq.split("-"))
        for num in range(start, end+1):
            num_str = str(num)
            l = len(num_str)
            
            for n in range(1,int(l/2)+1):
                arr = [(num_str[i:i+n]) for i in range(0, l, n)]
                if check(arr):
                    count += num
                    break

    return count

print(second(test))
print(second(data))
