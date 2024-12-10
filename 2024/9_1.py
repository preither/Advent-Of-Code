with open('input.txt') as f:
    map = list(map(int, list(f.readlines()[0][:-1])))

val_l = 0
val_h = int(len(map)/2)

point_l = 0
point_h = len(map) - 1

cnt = 0
s = 0

while True:
    #check low pointer
    if map[point_l] == 0:
        point_l += 1
        if point_l > point_h:
            break

    if point_l %2 == 0:
        s += cnt * val_l
        map[point_l] -= 1
    else:
        s += cnt * val_h
        map[point_h] -= 1
        map[point_l] -= 1

        #check high pointer
        if map[point_h] == 0:
            point_h -= 2
            val_h -= 1
            if map[point_h] == 0:
                break
    
    #check low pointer
    if map[point_l] == 0:
        point_l += 1
        if point_l %2 != 0:
            val_l += 1
        if point_l > point_h:
            break
    

    cnt += 1

print(s)


