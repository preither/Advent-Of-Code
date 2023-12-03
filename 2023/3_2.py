def find_beginning(c,i,j):
    if j == 0:
        return 0
    elif c[i][j-1].isdecimal():
        return find_beginning(c,i,j-1)
    else:
        return j

def get_number(c,i,start):
    num = ""
    pos = start
    while c[i][pos].isdecimal():
        num = num + c[i][pos]
        c[i][pos] = "."
        pos += 1
        if pos >= len(c[i]):
            break

    return int(num)

def check_field(c, i, j):
    try:
        if c[i][j].isdecimal():
            start = find_beginning(c,i,j)
            return get_number(c,i,start)
    except Exception as e: print(e)
    return 0

class Object:
    cnt = 0
    p = 1

def increase_cnt_and_sum(o, v):
    if v == 0:
        return
    o.cnt += 1

    if o.cnt > 2:
        return
    
    o.p *= v

def check_surrounding(c, i, j):
    o = Object()
    v = check_field(c,i-1,j)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i-1,j-1)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i,j-1)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i+1,j-1)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i+1,j)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i+1,j+1)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i,j+1)
    increase_cnt_and_sum(o, v)
    v = check_field(c,i-1,j+1)
    increase_cnt_and_sum(o, v)

    if o.cnt == 2:
        return o.p
    else:
        return 0


with open('input.txt') as f:
    c = f.readlines()

field = []
for i in range(len(c)):
    field.append([])
    for j in range(len(c[0])-1):
        field[i].append(c[i][j])

s = 0

for i in range(len(field)):
    for j in range(len(field[0])):
        v = field[i][j]
        if v == "*":
            s += check_surrounding(field,i,j)

print(s)

