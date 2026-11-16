import networkx as nx

file = open("input5.txt", "r").read()
# file = open("input5t.txt", "r").read()

# reformate the input to get rules and updates
lines = file.splitlines()
sep = lines.index('')
rules = lines[:sep]
updates = lines[sep+1:]


# ---------------------------------------------------------
# first attemp
# ---------------------------------------------------------

# get set of numbers
numbers = set([])
for rule in rules:
    r = rule.split("|")
    numbers.add(int(r[0]))
    numbers.add(int(r[1]))


# create dict with rules and dict with indices
dicts = []
indices = {}

for i, num in enumerate(numbers):
    dic = {
        "name" : num,
        "before" : [],
        "after" : []
    }
    indices[str(num)] = i
    dicts.append(dic)

# fill in rules
for rule in rules:
    r = rule.split("|")
    first = r[0]
    second = r[1]
    dicts[indices[first]]["after"].append(second)
    dicts[indices[second]]["before"].append(first)


# check rules and update score
score = 0
false_update = []
for update in updates:
    is_good = True
    nums = update.split(",")
    l = len(nums)
    center = nums[int(l/2)]

    for i in range(l): # go trough current update
        current = nums[i]
        before = nums[:i]
        after = nums[i+1:]
        for n in before: # check if numbers before is in is forbidde
            if n in dicts[indices[current]]["after"]:
                is_good = False
        for n in after: # check if numbers after current number is forbidden
            if n in dicts[indices[current]]["before"]:
                is_good = False

    if is_good: # update if update is good
        score += int(center)
    else: 
        false_update.append(update)

print(score)

# for d in dicts:
#     print(d)

# Aufgabe 2. erstelle Graf und damit topologische Sortierung


# ---------------------------------------------------------
# second attemp
# ---------------------------------------------------------

# First puzzle
# create graph
G = nx.DiGraph()
edges = []
for rule in rules:
    split = rule.split("|")
    edges.append((int(split[0]), int(split[1])))
G.add_edges_from(edges)

score1 = 0
falses = []
for update in updates:
    nums = update.split(",")
    nodes = list(map(int, nums))
    good = True

    for i in range(len(nodes)-1):
        for j in range(i+1, len(nodes)):
            if not G.has_edge(nodes[i], nodes[j]):
                good = False

    if good:
        score1 += int(nums[int(len(nums)/2)]) # add center value
    else:
        falses.append(nodes) # add to falses list


# second puzzle
# create subgraph and apply topological sorting
score2 = 0
for f in falses:
    sub = nx.subgraph(G, f)
    temp = list(nx.topological_sort(sub))
    score2 += temp[int(len(temp)/2)]

print(score1)
print(score2)