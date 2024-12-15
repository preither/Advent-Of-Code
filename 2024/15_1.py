def move_field(map, pos, new_pos, field):
    map[new_pos[0]][new_pos[1]] = field
    map[pos[0]][pos[1]] = "."

def move_box(map, new_pos, d):
    new_box_pos = new_pos[0] + directions[d][0], new_pos[1] + directions[d][1]

    if map[new_box_pos[0]][new_box_pos[1]] == "#":
        return False
    elif map[new_box_pos[0]][new_box_pos[1]] == ".":
        move_field(map, new_pos, new_box_pos, "O")
        return True
    else:
        #here is a box check the next one
        move_posible = move_box(map, new_box_pos, d)

        if move_posible:
            move_field(map, new_pos, new_box_pos, "O")
            return True
        else:
            return False

with open('input.txt') as f:
    contents = f.readlines()

warehouse = []
instructions = []
for c in contents:
    if c[0] == "#":
        warehouse.append(list(c[:-1]))
    elif len(c) > 1:
        instructions.append(c[:-1])

pos = (0,0)

for y in range(len(warehouse)):
    for x in range(len(warehouse[0])):
        if warehouse[y][x] == "@":
            pos = (y,x)
            break

directions = {
    "<": ( 0,-1),
    ">": ( 0, 1),
    "^": (-1, 0),
    "v": ( 1, 0)
}


for i in instructions:
    for d in i:
        new_pos = (pos[0] + directions[d][0], pos[1] + directions[d][1])

        if warehouse[new_pos[0]][new_pos[1]] == ".":
            #empty field just move
            move_field(warehouse, pos, new_pos, "@")
            pos = new_pos
        elif warehouse[new_pos[0]][new_pos[1]] == "O":
            if move_box(warehouse, new_pos, d):
                move_field(warehouse, pos, new_pos, "@")
                pos = new_pos


val = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[0])):
        if warehouse[y][x] == "O":
            val += 100*y +x

print(val)
