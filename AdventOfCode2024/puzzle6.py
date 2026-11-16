import numpy as np
# np.set_printoptions(threshold=np.inf)



def is_inside(index: tuple, dim: tuple):
    x = index[0]
    y = index[1]

    inside = True

    if x < 0 or x > dim[0]:
        inside = False
    if y < 0 or y > dim[1]:
        inside = False

    return inside

def go(index: tuple, mat: np.matrix):
    # index is where we want to go
    directions = ["up", "right", "down", "left"]
    if mat[index[0], index[1]] != "#":
        pass
    pass
    # TODO finish this




# file = open("input6.txt", "r").read()
file = open("input6t.txt", "r").read()
lines = file.splitlines()

# get matrix
arr = []
for line in lines:
    arr.append([x for x in line])
mat = np.matrix(arr, dtype=str)

# get start index
start = np.where(mat == "^")
start = (int(start[0][0]), int(start[1][0]))



# initialize
visited = mat.copy()
current = start
count = 0
direction = "up"

# start loop
while is_inside(current, mat.shape):
    print(current)
    visited[current[0], current[1]] = "X"
    # TODO use go() function and finish this

    match direction:
        case "up":
            pass
        case "down":
            pass
        case "right":
            pass
        case "left":
            pass
        


    current = (current[0] -1, current[1] -1)
    

print(len(np.where(visited == "X")[0]))

# print(visited)
# print(mat)