def get_number(string):
    number = []
    count = 0
    for char in string:
        if char.isnumeric():
            number.append(char)
    if (len(number) > 0):
        count += int(number[0] + number[-1])
    return count

def find_numbers(string):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    indices = []
    first_number = 0
    second_number = 0

    # vorwärts
    new_string = string
    for i, n in enumerate(nums):
        indices.append([new_string.find(n), i])
    indices = sorted(indices)

    for t in indices:
        if t[0] != -1:
            new_string = new_string.replace(nums[t[1]], str(t[1] +1))

    for char in new_string:
        if char.isnumeric():
            first_number = char
            break 

    # rückwärts
    new_string = string
    for i, n in enumerate(nums):
        indices.append([new_string.find(n), i])
    indices = sorted(indices, reverse=True)

    for t in indices:
        if t[0] != -1:
            new_string = new_string.replace(nums[t[1]], str(t[1] +1))

    for char in reversed(new_string):
        if char.isnumeric():
             second_number = char 
             break

    return int(first_number + second_number)


f = open("Input/input01.txt", "r")
# Aufgabe 1
count = 0
for line in f:
    count += get_number(line)
# print(count)

# Aufgabe 2
f = open("Input/input01.txt", "r")
# Lösung ist falsch aber keine Ahnung wieso. da soetwas wie "sevenine" als 79 und 
# ähnliches richtig gemacht wird

# f = open("Input/test01.txt", "r")
count2 = 0
# for line in f:
#     count2 += find_numbers(line)





## neue Idee
for line in f:
    indices = []
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for n in nums:
        i = line.find(n)
        if i != -1:
            indices.append([i, n])
    indices.sort()

    first_number = indices[0][1]
    second_number = indices[-1][1]
    if first_number.isnumeric():
        first_number = int(first_number)
    else:
        first_number = nums.index(first_number) + 1
    if second_number.isnumeric():
        second_number = int(second_number)
    else:
        second_number = nums.index(second_number) + 1
    

    # print(indices)
    # print(first_number)
    # print(second_number)
    count2 += int(str(first_number) + str(second_number))




print(count2)