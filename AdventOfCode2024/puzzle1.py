import numpy as np

# 1.
# get right and left
file = open("input1.txt", "r")

right = []
left = []

for line in file:
    temp = line.split("   ")
    right.append(int(temp[1]))
    left.append(int(temp[0]))

right.sort()
left.sort()
right_arr = np.array(right)
left_arr = np.array(left)

# get difference sum
diff = np.absolute(left_arr - right_arr)
sum = np.sum(diff)

print("1. ", sum)


# 2. 
similarity_score = 0

for num in left_arr:
    indices = np.where(right_arr == num)[0] # get indices of same numbers
    similarity_score += num * len(indices) # update the score


print("2. ", similarity_score)

file.close()