
import re

def get_number(string: str) -> int:
    nums = re.findall(r'\d+', string)
    return int(nums[0]) * int(nums[1])


# file = open("input3t.txt", "r").read()
file = open("input3.txt", "r").read()

score = 0
muls = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', file)
for mul in muls:
    score += get_number(mul)

print(score)


score_do = 0 
from_do_to_dont = re.split(r'don\'t\(\)', file) # split at don't()

for section in from_do_to_dont:
    # go trough all sections splitted by don't() and split again at do()
    do_sec = re.split(r'do\(\)', section)
    if len(do_sec) > 1:
        # if there is at least one "do()" add all numbers after first "do()"
        for i in range(1, len(do_sec)):
            muls_do = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', do_sec[i])
            for mul in muls_do:
                score_do += get_number(mul)

print(score_do)

