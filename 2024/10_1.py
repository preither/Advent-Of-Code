def check_field(map, position, direction):
    max_height = len(map) - 1
    max_width = len(map[0]) - 2

    field_to_check = (position[0] + direction[0], position[1] + direction[1])

    if field_to_check[0] < 0 or field_to_check[0] > max_height or field_to_check[1] < 0 or field_to_check[1] > max_width:
        return False
    
    if int(map[field_to_check[0]][field_to_check[1]]) - int(map[position[0]][position[1]]) == 1:
        return True
    
    return False

with open('input.txt') as f:
    contents = f.readlines()

directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]

cnt = 0
for y in range(len(contents)):
    for x in range(len(contents[0][:-1])):
        if contents[y][x] != "0":
            continue
        nodes= [(y,x)]
        nines= []

        while len(nodes) > 0:
            new_nodes = []
            for n in nodes:
                for d in directions:
                    if check_field(contents, n, d):
                        new = (n[0]+d[0], n[1]+d[1])
                        if contents[n[0]][n[1]] == "8":
                            if not new in nines:
                                nines.append(new)
                        else:
                            if not new in new_nodes:
                                new_nodes.append((n[0]+d[0], n[1]+d[1]))

            nodes = new_nodes
        cnt += len(nines)

print(cnt)
