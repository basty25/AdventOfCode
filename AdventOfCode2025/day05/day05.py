import numpy as np
from pprint import pprint as print


def load(path):
    # load data
    ranges = []
    values = []
    with open(path) as f:
        empty = False
        for line in f.readlines():
            if line == "\n":
                empty = True
                continue
            if not empty:
                start, end = line.strip().split("-")
                ranges.append([int(start), int(end)])
            else:
                values.append(line.strip())
    return ranges, values

def first(path):
    ranges, values = load(path)
    # create available set
    count = 0
    for num in values:
        for r in ranges:
            start, end = r[0], r[1]
            if int(num) >= start and int(num) <= end:
                count += 1
                break
    print(count)

# first("day05/test05.txt")
# first("day05/input05.txt")


def second(path):
    ranges, _ = load(path)
    m = 0
    count = 0

    print(sorted(ranges))
    for r in sorted(ranges):
        start, end = r[0], r[1]
        if m < start:
            count += end+1 - start
            print("no overlap")
        if m >= start and m <= end:
            count += end - m
            print("overlap")
        m = end
    print(count)

    # ranges = sorted(ranges)
    # for i in range(len(ranges)):
    #     ranges[i] = [ranges[i][0], ranges[i][1], ranges[i][1] + 1 - ranges[i][0]]

    # print(ranges)


        

second("day05/test05.txt")
second("day05/input05.txt")

# test = np.genfromtxt("day05/test05.txt", dtype=str, replace_space="#")
# print(test)
