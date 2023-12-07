with open('input.txt') as f:
    c = f.readlines()

vals = []
vals_next = []

for i in c:
    if "seeds:" in i:
        vals_raw = list(map(int, i[:-1].split(": ")[1].split(" ")))
        for j in range(len(vals_raw)):
            if j % 2 == 0:
                vals.append([vals_raw[j], vals_raw[j]+ vals_raw[j+1] - 1])
    elif ":" in i:
        for j in vals:
            vals_next.append(j)
        vals = vals_next.copy()
        vals_next = []
    elif len(i) > 1:
        line = list(map(int,i[:-1].split(" ")))
        dest = line[0]
        src = line[1]
        rang = line[2]
        offset = dest - src
        
        while 1:
            val_copy = vals.copy()
            new_arr = []
            for v in vals:
                if v[0] in range(src, src + rang) and v[1] in range(src, src + rang):
                    vals_next.append([v[0] + offset, v[1] + offset])
                    val_copy.remove(v)
                elif v[0] in range(src, src + rang):
                    end = src + rang - 1
                    vals_next.append([v[0] + offset, end + offset])
                    new_arr.append([end+1, v[1]])
                    val_copy.remove(v)
                elif v[1] in range(src, src + rang):
                    start = src
                    vals_next.append([start + offset, v[1] + offset])
                    new_arr.append([v[0], src-1])
                    val_copy.remove(v)
            
            vals = val_copy.copy()
            if len(new_arr) == 0:
                break
            else:
                for n in new_arr:
                    vals.append(n)

for j in vals:
    vals_next.append(j)
    vals = vals_next.copy()

print(min(vals)[0])
    