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

first = True
cnt = 1
s = 0
for l in lines:
    if l != "\n":
        if first:
            a = eval(l[:-1])
            first = False
        else: 
            b = eval(l[:-1])
            if check(a,b) == Result.Right:
                s+= cnt

    else:
        first = True
        cnt += 1

print(s)