import numpy as np
import re

test = np.genfromtxt("day06/test06.txt", dtype=str, unpack=True)
data = np.genfromtxt("day06/input06.txt", dtype=str, unpack=True)
# print(test)

def first(data):
    count = 0
    for line in data:
        temp = 1
        for i in range(len(line)-1):
            if line[-1] == "+":
                count += int(line[i])
            else:
                temp *= int(line[i])
        if line[-1] == "*":
            count += temp
            
    print(count)


# first(test) 
# first(data) 

def second(path):
    # get data
    data = []
    with open(path) as f:
        for line in f.readlines():
            data.append(line)
    # get lenghts of numbers
    lenghts = re.findall(r"\s+", data[-1])
    for i in range(len(lenghts)):
        lenghts[i] = len(lenghts[i])

    # adjust for end of file
    lenghts[-1] += 1

    # get data in matricies
    i = 0
    new_data = []
    for j in range(len(lenghts)):
        block = []
        for k in range(len(data)):
            s = "".join(data[k][i:i+lenghts[j]])
            block.append(s)
        new_data.append(block)
        i += lenghts[j] +1


    # get counts
    count = 0
    # create matrix of the strings and update the count with the operation stored in line[-1]
    for line in new_data:
        mat = np.array([list(x) for x in line[:-1]])
        t = 1
        for num in mat.T:
            n = int("".join(num))
            if line[-1].strip() == "+":
                count += n
            else:
                t *= n
            
        if line[-1].strip() == "*":
            count += t

    print(count)



second("day06/test06.txt")
second("day06/input06.txt")
