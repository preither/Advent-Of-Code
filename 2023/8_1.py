with open('input.txt') as f:
    c = f.readlines()

directions = []
for i in c[0][:-1]:
    if i == "L":
        directions.append(0)
    else:
        directions.append(1)

paths = {}

for path in c[2:]:
    split = path[:-1].split(" = ")
    start = split[0]
    to = split[1][1:-1].split(", ")
    paths[start] = [to[0], to[1]]

pos = "AAA"
cnt = 0
finish = False
while not finish:
    for d in directions:
        cnt += 1
        pos = paths[pos][d]
        if pos == "ZZZ":
            finish = True
            break

print(cnt)