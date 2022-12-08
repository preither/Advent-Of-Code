with open('input.txt') as f:
    contents = f.readlines()

stacks = []

max_crate = 0
nr_piles = 0
for i in range(len(contents)):
    if contents[i][1] == "1":
        max_crate = i
        nr_piles = len(contents[i]) / 4
        break

for i in range(nr_piles):
    stacks.append([])

for h in range(max_crate):
    for l in range(nr_piles):
        crate = contents[h][1 + l * 4]
        if crate != " ":
            stacks[l].append(crate)


for line in contents:
    splitted = line.split(" ")
    if splitted[0] == "move":
        nr = int(splitted[1])
        fro = int(splitted[3]) -1
        to = int(splitted[5]) - 1

        for i in range(nr):
            element = stacks[fro].pop(0)
            stacks[to].insert(i, element)

str = ""

for i in range(nr_piles):
    str += stacks[i][0]

print(str)