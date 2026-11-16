
elves = []
f = open("input01.txt", "r")

temp = []

for line in f.readlines():
    if(line == "\n"):
        elves.append(temp)
        temp = []
        continue
    temp.append(int(line))

numbers = []
count = 0
for items in elves:
    for item in items:
        count += item
    numbers.append(count)
    count = 0

result1 = max(numbers)


# Part 2
topthree = []
topthree.append(max(numbers))
numbers.remove(max(numbers))
topthree.append(max(numbers))
numbers.remove(max(numbers))
topthree.append(max(numbers))
numbers.remove(max(numbers))

result2 = topthree[0] + topthree[1] + topthree[2]
print(result2)