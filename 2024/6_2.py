import copy

with open('test.txt') as f:
    contents = f.readlines()


pos = (0,0)
direction = (0, -1)
mapping = []

for c in contents:
    mapping.append(list(c[:-1]))

height = len(mapping)
width = len(mapping[0])

for y in range(height):
    for x in range(width):
        if mapping[y][x] == "^":
            pos = (x, y)
            mapping[y][x] = "X"

mapping_save = copy.deepcopy(mapping)
pos_save = pos

cnt = 0
while True:
    new_x = pos[0] + direction[0]
    new_y = pos[1] + direction[1]

    try:
        if mapping[new_y][new_x] == ".":
            mapping[new_y][new_x] = "X"
            pos = (new_x, new_y)
        elif mapping[new_y][new_x] == "X":
            pos = (new_x, new_y)
        elif mapping[new_y][new_x] == "#":
            #rotate 90 degrees
            direction = (-direction[1], direction[0])
    except:
        break

cnt = 1
for y in range(height):
    for x in range(width):
        if mapping[y][x] != "X" or (y == pos[1] and x == pos[1]):
            continue
        #make empty directions
        directions = []
        for y_d in range(height):
            directions.append([])
            for x_d in range(width):
                directions[y_d].append([])

        draw_map = copy.deepcopy(mapping_save)
        draw_map[y][x] = "#"
        pos = pos_save
        direction = (0, -1)

        while True:
            new_x = pos[0] + direction[0]
            new_y = pos[1] + direction[1]
            if new_x < 0 or new_y < 0:
                break
            
            directions[pos[1]][pos[0]].append(direction)
            try:
                if draw_map[new_y][new_x] == ".":
                    draw_map[new_y][new_x] = "X"
                    pos = (new_x, new_y)
                elif draw_map[new_y][new_x] == "X":
                    pos = (new_x, new_y)
                elif draw_map[new_y][new_x] == "#":
                    #rotate 90 degrees
                    direction = (-direction[1], direction[0])

                if direction in directions[new_y][new_x]:
                    cnt += 1
                    
                    break
            except:
                break       

print(cnt)