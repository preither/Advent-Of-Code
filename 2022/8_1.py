with open('input.txt') as f:
    contents = f.readlines()

cnt = 2 * (len(contents[0]) - 2) + 2* (len(contents) -1)
for x in range(len(contents[0]) -2):
    for y in range(len(contents) - 1):
        if x > 0 and y > 0:
            val = contents[y][x]
            fail = False
            for i in range(len(contents[0]) -1):
                if i == x:
                    if fail == False:
                        cnt += 1
                        break
                    else:
                        fail =False
                elif contents[y][i] >= val:
                    fail = True
                if i == len(contents[0]) -1 - 1:
                    if fail == False:
                        cnt += 1
            if fail == True:
                fail = False
                for i in range(len(contents)):
                    if i == y:
                        if fail == False:
                            cnt += 1
                            break
                        else:
                            fail =False
                    elif contents[i][x] >= val:
                        fail = True
                    if i == len(contents) - 1:
                        if fail == False:
                            cnt += 1
            




print(cnt)