with open('input.txt') as f:
    c = f.readlines()

directions = []
for i in c[0][:-1]:
    if i == "L":
        directions.append(0)
    else:
        directions.append(1)

paths = {}

start_pos = []

for path in c[2:]:
    split = path[:-1].split(" = ")
    start = split[0]
    to = split[1][1:-1].split(", ")
    paths[start] = [to[0], to[1]]
    if start[-1] == "A":
        start_pos.append(start)

cnts = []
for pos in start_pos:
    finish = False
    cnt = 0
    while not finish:
        for d in directions:
            cnt += 1
            pos = paths[pos][d]
            if pos[-1] == "Z":
                finish = True
                break
    cnts.append(cnt)
    

#gibt Wege raus ->mit Online Rechner kgV bilden
print(cnts)