from functools import cmp_to_key

class Result():
    Right = 1
    NRigth = 2
    Equal = 3

def check(a, b):
    #print("compare ", a, b)
    if not type(a) is list and not type (b) is list:
        if a == b:
            return Result.Equal
        if a < b:
            return Result.Right
        else:
            return Result.NRigth
    else:
        if type(a) is list:
            if type(b) is list:
                for i in range(len(a)):
                    if i >= len(b):
                        return Result.NRigth
                    v = check(a[i], b[i])
                    if v != Result.Equal:
                        return v
                if len(b) > len(a):
                    return Result.Right
                return Result.Equal
            else:
                return check(a,[b])
        else:
            return check([a], b)



f = open('input.txt', 'r')
lines = f.readlines()

two = [[2]]
six = [[6]]
all = [2, 6]
for l in lines:
    if l != "\n":
        a = eval(l[:-1])
        cnt = 0
        inserted = False
        for i in all:
            if check(a, i) == Result.Right:
                all.insert(cnt, a)
                inserted =True
                break
            cnt += 1
        if not inserted:
            all.append(a)

    
val = 1

cnt = 1
for i in all:
    if check(two, i) == Result.Equal:
        val *= cnt
    elif check(six, i) == Result.Equal:
        val *= cnt
    cnt += 1

print(val)