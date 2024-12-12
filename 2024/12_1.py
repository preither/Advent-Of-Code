def check_field(map, already_checked, position, field_to_check):
    max_height = len(map) - 1
    max_width = len(map[0]) - 2

    if field_to_check[0] < 0 or field_to_check[0] > max_height or field_to_check[1] < 0 or field_to_check[1] > max_width:
        return False
    
    if field_to_check in already_checked:
        return False 
    
    if map[field_to_check[0]][field_to_check[1]] == map[position[0]][position[1]]:
        return True
    
    return False

with open('input.txt') as f:
    contents = f.readlines()

directions = [(0, 1),(0, -1),(1, 0),(-1, 0)]
already_visited = []

cnt = 0
for y in range(len(contents)):
    for x in range(len(contents[0][:-1])):
        if (y,x) in already_visited:
            continue

        already_visited.append((y,x))
        nodes= [(y,x)]
        already_cnt = [(y,x)]
        perimeter = 0
        area = 1        

        while len(nodes) > 0:
            new_nodes = []
            for n in nodes:
                for d in directions:
                    field_to_check = (n[0] + d[0], n[1] + d[1])
                    if check_field(contents, already_cnt, n, field_to_check):
                        area += 1
                        already_cnt.append(field_to_check)
                        new_nodes.append(field_to_check)
                        already_visited.append(field_to_check)
                    else:
                        if not field_to_check in already_cnt:
                            perimeter += 1

            nodes = new_nodes
        cnt += area * perimeter

print(cnt)
