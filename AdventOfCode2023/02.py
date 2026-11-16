f = open("Input/input02.txt", "r")
# f = open("Input/test02.txt", "r")

# Aufgabe 1
count = 0
ges_power = 0
erlaubt = [12, 13, 14]
for index, line in enumerate(f):
    add = True
    game = line.split(":")
    game = game[1].strip()
    mengen = game.split(";")

    # for sets in menge:
    for i in range(len(mengen)):
        set = [0, 0, 0] # [rot, gruen, blau]
        neu = []
        temp = mengen[i].split(",")
        for item in temp:
            item = item.strip()
            temp2 = item.split(" ")
            if temp2[1] == "blue":
                set[2] = int(temp2[0])
            if temp2[1] == "red":
                set[0] = int(temp2[0])
            if temp2[1] == "green":
                set[1] = int(temp2[0])
            
        # print(temp2) 
        mengen[i] = set


    for set in mengen:
        for i in range(len(set)):
            if set[i] > erlaubt[i]:
                add = False
    
    if add:
        count += index + 1
    

    # print(mengen)

    minimal = [0, 0, 0]
    for set in mengen:
        for i in range(0, 3):
            if minimal[i] < set[i]:
                minimal[i] = set[i]
    # print(minimal)
    power = minimal[0] * minimal[1] * minimal[2]
    # print(power)
    ges_power += power



print(count)
print(ges_power)