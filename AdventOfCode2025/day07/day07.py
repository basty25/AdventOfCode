from pprint import pprint 
import numpy as np

test = np.genfromtxt("day07/test07.txt", dtype=str, delimiter=1)
data = np.genfromtxt("day07/input07.txt", dtype=str, delimiter=1)


def first(data: np.array):
    idx_start = np.where(data[0] == "S")[0].tolist()
    beams = [idx_start]
    hats = []
    data[1][idx_start] = "|"
    count = 0
    new_data = data.copy()
    for i in range(2, len(data), 2):
        # skip first two rows
        if i == 0 or i == 1:
            continue

        hats_in_line = np.where(data[i] == "^")[0].tolist()

        new_beams = []
        for beam in beams[i//2 -1]:
            if beam in hats_in_line:
                count += 1
                # --------- normal 
                left, right = beam -1, beam +1
                if left not in new_beams:
                    new_beams.append(left)
                if right not in new_beams:
                    new_beams.append(right)
            else:
                if beam not in new_beams:
                    new_beams.append(beam)

        # create new_data
        for beam in new_beams:
            new_data[i][beam] = "|"
            new_data[i+1][beam] = "|"
                
        beams.append(new_beams)
        hats.append(hats_in_line)
    
    print(count)
    return beams, hats, new_data

# first(test)
# first(data)

def second(data):
    _, _, new_dat = first(data)

    s = np.array(new_dat).shape

    c = new_dat.copy()
    c = np.zeros(s)
    for i in range(1, s[0]):
        for j in range(1, s[1]-1):
            # do something at "|"
            if new_dat[i, j] == "|":
                # start 
                # up left right
                if new_dat[i-1, j] == "|" and new_dat[i, j-1] == "^" and new_dat[i, j+1] =="^":
                    c[i, j] = c[i-1, j] + c[i-1, j-1] + c[i-1, j+1]
                # left right
                elif new_dat[i, j-1] == "^" and new_dat[i, j+1] == "^": 
                    c[i, j] = c[i-1, j-1] + c[i-1, j+1]
                # up right
                elif new_dat[i-1, j] == "|" and new_dat[i, j+1] == "^":
                    c[i, j] = c[i-1, j] + c[i-1, j+1]
                # up left
                elif new_dat[i-1, j] == "|" and new_dat[i, j-1] == "^":
                    c[i, j] = c[i-1, j] + c[i-1, j-1]
                # S
                elif new_dat[i-1, j] == "S":
                    c[i, j] = 1
                # right
                elif new_dat[i, j+1] == "^": 
                    c[i, j] = c[i-1, j+1]
                # left
                elif new_dat[i, j-1] == "^": 
                    c[i, j] = c[i-1, j-1]
                # up
                elif new_dat[i-1, j] == "|":
                    c[i, j] = c[i-1, j]

    print(int(sum(c[-1])+2))

second(test)
second(data)



# for beam in beams:
#     print(beam)
# for hat in hats:
#     print(hat)








# plot beams
# for beam in beams:
#     for i in range(15):
#         if i in beam:
#             print("|", end="")
#         else:
#             print(".", end="")
#     print()

# plot hats
# for hat in hats:
#     for i in range(15):
#         if i in hat:
#             print("^", end="")
#         else:
#             print(".", end="")
#     print()


