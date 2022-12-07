f = open('input.txt', 'r')
lines = f.readlines()

dic = {}

dics = []

cnt = 0
for l in lines:
    split = l[:-1].split(" ")
    try:
        nr = int(split[0])
        dic[dics[-1]] += nr
    except:
        if split[1] == "cd":
            if split[2] == "..":
                dic[dics[-2]] += dic[dics[-1]]
                dics.pop()
            else:
                name = split[2] + str(cnt)
                dics.append(name)
                dic[name] = 0
                cnt += 1

for i in range(len(dics)):
    idx = len(dics) - 1 - i

    if idx >= 1:
        dic[dics[idx-1]] += dic[dics[idx]]
        
needed = 30000000 - (70000000 - dic[dics[0]])
m = 1e9
for a in dic:
    if dic[a] >= needed and dic[a] < m:
        m=dic[a]
print(m)
