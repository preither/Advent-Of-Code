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
                y1 = yA - (yB - yA)
                x1 = xA - (xB - xA)
                y2 = yB - (yA - yB)
                x2 = xB - (xA - xB)

                if y1 >= 0 and y1 < over_y and x1 >= 0 and x1 < over_x:
                    if not (y1, x1) in antinodes:
                        antinodes.append((y1, x1)) 
                if y2 >= 0 and y2 < over_y and x2 >= 0 and x2 < over_x:
                    if not (y2, x2) in antinodes:
                        antinodes.append((y2, x2)) 

print(len(antinodes))
