with open('input.txt') as f:
    contents = f.readlines()
positions= {}

over_y = len(contents) 
over_x = len(contents[0][:-1])

for y in range (over_y):
    for x in range(over_x):
        val = contents[y][x]
        if val != ".":
            try:
                positions[val].append((y,x))
            except:
                positions[val] = []
                positions[val].append((y,x))



antinodes = []

for node in positions:
    for i in range(len(positions[node])):
        for j in range(1, len(positions[node])):
            yA = positions[node][i][0]
            xA = positions[node][i][1]
            yB = positions[node][j][0]
            xB = positions[node][j][1]
            if i != j:
                v1 = (yB - yA, xB - xA)
                
                multipliers = [1, -1]
                
                if not (yA, xA) in antinodes:
                    antinodes.append((yA, xA))
                if not (yB, xB) in antinodes:
                    antinodes.append((yB, xB))

                for mult in multipliers:
                    while(True):
                        pos = (yA + mult * v1[0], xA + mult * v1[1])

                        if pos[0] < 0 or pos[0] >= over_y or pos[1] < 0 or pos[1] >= over_x:
                            #out of bound
                            break
                        elif not pos in antinodes:
                            antinodes.append(pos)

                        if mult > 0:
                            mult += 1
                        else:
                            mult -= 1

print(len(antinodes))
