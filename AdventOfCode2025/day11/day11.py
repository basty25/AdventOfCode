import numpy as np
from pprint import pprint

# test = np.genfromtxt("day11/test11.txt", delimiter=" ")
# print(test)

def first(file_path):
    # get data
    data = []
    with open(file_path) as file:
        for line in file.readlines():
            line = line.strip().split(" ")
            data.append([line[0][0:-1], line[1:]])


    # init count
    global count
    count = 0
    def find_path(path, current_path=[]):

        # define end condtion
        if path == "out":
            global count
            count += 1
            return 1
        # continuation part
        else:
            directions = [x[1] for x in data if x[0] == path]
            for dir in directions[0]:
                find_path(dir)

    # start recursion
    start = [x[1] for x in data if x[0] == "you"]
    for s in start[0]:
        find_path(s)

    # print count
    print(count)
    
    
first("day11/test11.txt")
first("day11/input11.txt")


def second(file_path):
    # get data
    data = []
    with open(file_path) as file:
        for line in file.readlines():
            line = line.strip().split(" ")
            data.append([line[0][0:-1], line[1:]])

    # init count
    global ways
    ways = []
    def find_path(path, current_path=[]):
        # print(current_path)
        # define end condtion
        if path == "out":
            global ways
            ways.append(current_path)
            return 1
        if path in current_path[:-1]:
            return 0
        # continuation part
        else:
            directions = [x[1] for x in data if x[0] == path]
            for dir in directions[0]:
                find_path(dir, current_path + [dir])

    # start recursion
    start = [x[1] for x in data if x[0] == "svr"]
    for s in start[0]:
        find_path(s, ["svr", s])

    # pprint(ways)
    # get count of the correct ways
    count = 0
    for p in ways:
        if "fft" in p and "dac" in p:
            count += 1
    print(count)

# does only work wor the test case. Not fast enough for the real input
second("day11/test11_2.txt")
# second("day11/input11.txt")
