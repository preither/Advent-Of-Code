def check_node(s, d):
    if d == "E":
        d = "z"
    if ord(d) - ord(s) <= 1:
        return True
    else:
        return False

f = open('input.txt', 'r')
lines = f.readlines()


x= 0
y= 0
for l in lines:
    for i in l:
        if i == "S":
            s = [x, y]
        if i == "E":
            e = [x, y]
        x += 1
    x = 0
    y += 1

max_x = len(lines[0]) - 1
max_y = len(lines) - 1

x_cnt= 0
y_cnt= 0
lowest = 1000
for l in lines:
    for a in l:
        if a == "a":
            found = False
            already_visited = []
            nodes = [[x_cnt, y_cnt]]
            cnt = 0
            while not found:
                new_nodes = []
                for n in nodes:
                    s = lines[n[1]][n[0]]
                    if s == "S":
                        s = "a"
                    #check right
                    x = n[0] + 1
                    y = n[1]
                    if x <= max_x:
                        r = lines[y][x]
                        if check_node(s, r):
                            new_nodes.append([x, y])
                    #check left
                    x = n[0] - 1
                    y = n[1]
                    if x >= 0:
                        r = lines[y][x]
                        if check_node(s, r):
                            new_nodes.append([x, y])
                    
                    #check down
                    x = n[0]
                    y = n[1] + 1
                    if y <= max_y:
                        r = lines[y][x]
                        if check_node(s, r):
                            new_nodes.append([x, y])
                    #check up
                    x = n[0]
                    y = n[1] - 1
                    if y >= 0:
                        r = lines[y][x]
                        if check_node(s, r):
                            new_nodes.append([x, y])

                nodes = []
                for n in new_nodes:
                    if n[0] == e[0] and n[1] == e[1]:
                        found = True
                        break
                    st = str(n[0]) + "_" +str(n[1])
                    if st not in already_visited:
                        nodes.append(n)
                        already_visited.append(st)

                cnt += 1
                if cnt >= lowest:
                    break
            if cnt < lowest:
                lowest = cnt
        x_cnt += 1
    x_cnt = 0
    y_cnt += 1

print(lowest)
        

