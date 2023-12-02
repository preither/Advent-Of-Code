cubes = {
    "r": 12,
    "g": 13,
    "b": 14
}

with open('input.txt') as f:
    c = f.readlines()

s = 0
for i in c:
    id = int(i.split(":")[0].split(" ")[1])
    draws = i.split(":")[1].split(";")

    
    valid = True
    for d in draws:
        words = d.split(" ")
        val = 0
        for w in words:
            if w == "" or w == ",":
                pass
            elif w.isnumeric():
                val = int(w)
            else:
                key = w[0]
                if val > cubes[key]:
                    valid = False
                    break
        if not valid:
            break
    
    if valid:
        s+= id

print(s)
