with open('input.txt') as f:
    c = f.readlines()

vals = []
vals_next = []

for i in c:
    if "seeds:" in i:
        vals = list(map(int, i[:-1].split(": ")[1].split(" ")))
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
        
        val_copy = vals.copy()
        for v in vals:
            if v in range(src, src + rang):
                vals_next.append(v + (dest - src))
                val_copy.remove(v)
        vals = val_copy.copy()

for j in vals:
    vals_next.append(j)
    vals = vals_next.copy()

print(min(vals))
    