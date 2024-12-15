def move_field(map, pos, new_pos, field):
    map[new_pos[0]][new_pos[1]] = field
    map[pos[0]][pos[1]] = "."

def move_box_vertical(map, new_box_pos_l, new_box_pos_r, d):
    map[new_box_pos_l[0]][new_box_pos_l[1]] = "["
    map[new_box_pos_r[0]][new_box_pos_r[1]] = "]"
    if directions[d][0] > 0:
        map[new_box_pos_l[0]-1][new_box_pos_l[1]] = "."
        map[new_box_pos_r[0]-1][new_box_pos_r[1]] = "."
    else:
        map[new_box_pos_l[0]+1][new_box_pos_l[1]] = "."
        map[new_box_pos_r[0]+1][new_box_pos_r[1]] = "."

def move_box(map, new_pos, d, move):
    if directions[d][0] == 0:
        new_box_pos = (new_pos[0], new_pos[1] + 2*directions[d][1])

        if map[new_box_pos[0]][new_box_pos[1]] == "#":
            return False
        elif map[new_box_pos[0]][new_box_pos[1]] == ".":
            if directions[d][1] > 0:
                map[new_pos[0]][new_pos[1]+1] = "["
                map[new_pos[0]][new_pos[1]+2] = "]"
                map[new_pos[0]][new_pos[1]] = "."
            else:
                map[new_pos[0]][new_pos[1]-1] = "]"
                map[new_pos[0]][new_pos[1]-2] = "["
                map[new_pos[0]][new_pos[1]] = "."

            return True
        else:
            #here is a box check the next one
            move_posible = move_box(map, new_box_pos, d, True)

            if move_posible:
                if directions[d][1] > 0:
                    map[new_pos[0]][new_pos[1]+1] = "["
                    map[new_pos[0]][new_pos[1]+2] = "]"
                    map[new_pos[0]][new_pos[1]] = "."
                else:
                    map[new_pos[0]][new_pos[1]-1] = "]"
                    map[new_pos[0]][new_pos[1]-2] = "["
                    map[new_pos[0]][new_pos[1]] = "."
                return True
            else:
                return False
    else:
        #move high we have to check two pos
        new_box_pos_l = (new_pos[0]+ directions[d][0], new_pos[1])
        new_box_pos_r = (new_pos[0]+ directions[d][0], new_pos[1] + 1)
        if map[new_pos[0]][new_pos[1]] == "]":
            new_box_pos_l = (new_box_pos_l[0], new_box_pos_l[1]-1)
            new_box_pos_r = (new_box_pos_r[0], new_box_pos_r[1]-1)

        if map[new_box_pos_l[0]][new_box_pos_l[1]] == "#" or map[new_box_pos_r[0]][new_box_pos_r[1]] == "#":
            return False
        elif map[new_box_pos_l[0]][new_box_pos_l[1]] == "." and map[new_box_pos_r[0]][new_box_pos_r[1]] == ".":
            if move:
                move_box_vertical(map, new_box_pos_l, new_box_pos_r, d)
            return True        
        #check left and right
        elif map[new_box_pos_l[0]][new_box_pos_l[1]] == "]" and map[new_box_pos_r[0]][new_box_pos_r[1]] == ".":
            if move_box(map, new_box_pos_l, d, True):
                if move:
                    move_box_vertical(map, new_box_pos_l, new_box_pos_r, d)
                return True
            else:
                return False
        
        elif map[new_box_pos_l[0]][new_box_pos_l[1]] == "." and map[new_box_pos_r[0]][new_box_pos_r[1]] == "[":
            if move_box(map, new_box_pos_r, d, True):  
                if move:
                    move_box_vertical(map, new_box_pos_l, new_box_pos_r, d)
                return True
            else:
                return False
        elif map[new_box_pos_l[0]][new_box_pos_l[1]] == "[" and map[new_box_pos_r[0]][new_box_pos_r[1]] == "]":
            if move_box(map, new_box_pos_r, d, True):  
                if move:
                    move_box_vertical(map, new_box_pos_l, new_box_pos_r, d)
                return True
            else:
                return False
        else:
            if move_box(map, new_box_pos_l, d, False) and move_box(map, new_box_pos_r, d, False):
                if move_box(map, new_box_pos_l, d, True) and move_box(map, new_box_pos_r, d, True):
                    if move:
                        move_box_vertical(map, new_box_pos_l, new_box_pos_r, d)
                    return True
            else:
                return False

with open('input.txt') as f:
    contents = f.readlines()

warehouse = []
instructions = []
for c in range(len(contents)):
    if contents[c][0] == "#":
        warehouse.append([])
        for i in contents[c]:
            if i == "#":
                warehouse[c].append("#")
                warehouse[c].append("#")
            elif i == "O":
                warehouse[c].append("[")
                warehouse[c].append("]")
            elif i == ".":
                warehouse[c].append(".")
                warehouse[c].append(".")
            elif i == "@":
                warehouse[c].append("@")
                warehouse[c].append(".")
    elif len(contents[c]) > 1:
        instructions.append(contents[c][:-1])

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
        elif warehouse[new_pos[0]][new_pos[1]] == "[" or warehouse[new_pos[0]][new_pos[1]] == "]":
            if move_box(warehouse, new_pos, d, True):
                move_field(warehouse, pos, new_pos, "@")
                pos = new_pos

        print(d)
        for w in warehouse:
            print(w)


val = 0
for y in range(len(warehouse)):
    for x in range(len(warehouse[0])):
        if warehouse[y][x] == "[":
            val += 100*y +x

print(val)
