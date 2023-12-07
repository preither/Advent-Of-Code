import math

with open('input.txt') as f:
    c = f.readlines()

inp = [[],[]]

cnt = 0
for i in c:
    vals = i[:-1].split(": ")[1].split(" ")
    for v in vals:
        if v != "":
            inp[cnt].append(int(v))
    cnt += 1
    
#t = time
#b = time button pressed
#d = (t-b) * b = -b² + t*b
#-b² + tb - d = 0
# b12 = -t + wurzel (t²-4d) / (-2) 

p = 1

for i in range(len(inp[0])):
    t = inp[0][i]
    d = inp[1][i]
    qh = (-t - math.sqrt(t*t - 4 * d)) / -2
    ql =  (-t + math.sqrt(t*t - 4 * d)) / -2

    qh_r = math.floor(qh)
    ql_r = math.ceil(ql)

    if qh_r - qh == 0:
        qh_r -= 1
    if ql_r - ql == 0:
        ql_r += 1
    p *= qh_r - ql_r + 1
    

print(p)
    