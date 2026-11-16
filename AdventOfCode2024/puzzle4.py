import re
import numpy as np

file = open("input4.txt", "r").read()
# file = open("input4t.txt", "r").read()

lines = file.splitlines()
dim = [len(lines[0]), len(lines)]

# function to get number of xmas in one string
def find_xmax(string: str) -> int:
    forward = len(re.findall(r'XMAS', string))
    backward = len(re.findall(r'XMAS', string[::-1]))
    return forward + backward

# function to get the colums
def get_colums(mat: np.matrix):
    dim = mat.shape
    colums = []
    for i in range(dim[1]):
        colum = ""
        for letter in mat[0:, i]:
            colum += str(letter[0, 0])
        colums.append(colum)
    return colums


def get_diag(mat: np.matrix):
    diagonals = []
    dim = mat.shape
    for i in range(-dim[0]+1, dim[0]):
        diag = np.diagonal(mat, i)
        word = ""
        for letter in diag:
            word += letter
        diagonals.append(word)
    return diagonals


# define matrix
arr = []
for line in lines:
    arr.append([x for x in line])
mat = np.matrix(arr)

# print(get_diag(mat))
# get colums, rows, and diagonals
colums = get_colums(mat)
diag1 = get_diag(mat)
diag2 = get_diag(np.fliplr(mat))



score = 0
for line in lines:
    score += find_xmax(line)
for colum in colums:
    score += find_xmax(colum)
for dia in diag1:
    score += find_xmax(dia)
for dia in diag2:
    score += find_xmax(dia)

print(score)



score2 = 0

# go through all possible centers
for i in range(1, dim[0]-1):
    for j in range(1, dim[1]-1):
        # first diag
        dia1 = False
        dia2 = False
        if (mat[i-1, j-1] == "M" and mat[i+1, j+1] == "S") or (mat[i-1, j-1] == "S" and mat[i+1, j+1] == "M"):
            dia1 = True
        if (mat[i-1, j+1] == "M" and mat[i+1, j-1] == "S") or (mat[i-1, j+1] == "S" and mat[i+1, j-1] == "M"):
            dia2 = True
        if dia1 and dia2 and mat[i, j] == "A":
            score2 += 1
        
print(score2)







