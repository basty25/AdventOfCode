
def is_good(line: list):
    # reverse the list if we go down
    if line[1] < line[0]:
        line.reverse()

    # get differences beetween the levels and check if they fullfill the conditions
    diffs = [line[i] - line[i+1] for i in range(len(line)-1)]
    for num in diffs:
        if num < -3 or num > -1:
            return False
    return True

def is_good_dampener(line: list):
    if is_good(line):
        return True

    for i in range(len(line)):
        if is_good(line[:i] + line[i+1:]):
            return True

file = open("input2.txt", "r")
# file = open("input2t.txt", "r")

safe_score = 0
safe_score_dampener = 0

for line in file:
    line_arr = [int(x) for x in line.split(" ")]

    # check other conditions
    if is_good(line_arr):
        safe_score += 1
    
    # check second conditions
    if is_good_dampener(line_arr):
        safe_score_dampener += 1

print(safe_score)
print(safe_score_dampener)

file.close()