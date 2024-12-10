with open('input.txt') as f:
    map = list(map(int, list(f.readlines()[0][:-1])))

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
        if map[point_l] < 0:
            cnt -= map[point_l]
            map[point_l] = 0
        else:
            s += cnt * int(point_l /2)
            map[point_l] -= 1
            cnt += 1
    else:
        found = False
        for i in range(0, point_h, 2):
            #search available
            index = point_h - i
            if index < point_l:
                break
            
            if map[index] <= map[point_l] and map[index] > 0:
                #found something that fits
                map[point_l] -= map[index]

                #add it to the sum
                for j in range(map[index]):
                    s += cnt * int(index/2)
                    cnt += 1

                map[index] = -map[index]           

                found = True

        if not found:
            cnt+= map[point_l]     
            point_l += 1       

    
    #check low pointer
    if map[point_l] == 0:
        point_l += 1
        if point_l >= point_h -1:
            break

print(s)


