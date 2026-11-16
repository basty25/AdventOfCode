f = open("input02.txt", "r")

score = 0

def isWin(char1, char2):
    if ((char1 == 'A' and char2 == 'Y') or (char1 == 'B' and char2 == 'Z') or (char1 == 'C' and char2 == 'X')):
        return 6
    else:
        return 0

def isDraw(char1, char2):
    if ((char1 == 'A' and char2 == 'A') or (char1 == 'B' and char2 == 'B') or (char1 == 'C' and char2 == 'C')):
        return 1
    else:
        return 0
    
def isLose(char1, char2):
    if ((char1 == 'A' and char2 == 'B') or (char1 == 'B' and char2 == 'C') or (char1 == 'C' and char2 == 'A')):
        return 1
    else:
        return 0

for line in f.readlines():
    score += isWin(line[0], line[2])
    score += isDraw(line[0], line[2])
    score += isLose(line[0], line[2]) 
    