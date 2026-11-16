

import numpy as np

test = np.loadtxt("day03/test03.txt", dtype=str)
data = np.loadtxt("day03/input03.txt", dtype=str)


def first(data):
    count = 0
    for line in data:
        nums = np.array(list(map(int,list(line)))) # convert to numpy array of digits
        m1 = np.max(nums[:-1]) # find max in array without last element
        index = np.argmax(nums[:-1]) # find argmax in array without last element
        m2 = np.max(nums[index+1:]) # find max in second part of array
        count += int(str(m1)+str(m2)) # add number to count

    return count


# print(first(test))
# print(first(data))



def second(data):
    count = 0
    for line in data:
        # initialize
        nums = np.array(list(map(int,list(line+"0")))) # convert to numpy array of digits
        maxes = []
        j = 0

        # compute joltages
        for i in range(0, 12):
            curr = nums[j+i:-12+i]
            idx = np.argmax(curr)
            maxes.append(np.max(curr))
            j += idx

        # reformat
        res = ""
        for n in maxes:
            res += str(n)
        count += int(res)

    return count

# print(second(test))
print(second(data))