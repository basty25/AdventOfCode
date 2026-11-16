import numpy as np
# f = open("Input/input03.txt", "r")
f = open("Input/test03.txt", "r")

mat = []
for line in f:
    row = []
    for c in line:
        if c != "\n":
            row.append(c)
    mat.append(row)

mat = np.matrix(mat, dtype="object")
dim = np.shape(mat)
print(dim)

def find_character(r, s, f, mat, dim):
    # check links
    found = False
    if s > 0:
        if mat[r, s -1] != ".":
            found = True
    # check rechts
    if f < dim[0]:
        if mat[r, f + 1] != ".":
            found = True
    # check oben 
    for i in range(s-1, f+1):
        pass
    
print(mat)