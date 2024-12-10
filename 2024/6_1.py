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

cnt = 1
while True:
    new_x = pos[0] + direction[0]
    new_y = pos[1] + direction[1]

    try:
        if mapping[new_y][new_x] == ".":
            mapping[new_y][new_x] = "X"
            cnt += 1
            pos = (new_x, new_y)
        elif mapping[new_y][new_x] == "X":
            pos = (new_x, new_y)
        elif mapping[new_y][new_x] == "#":
            #rotate 90 degrees
            direction = (-direction[1], direction[0])
    except:
        break

print(cnt)