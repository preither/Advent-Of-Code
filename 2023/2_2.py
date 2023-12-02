with open('input.txt') as f:
    c = f.readlines()

s = 0
for i in c:
    cubes = {
        "r": 0,
        "g": 0,
        "b": 0
    }
    id = int(i.split(":")[0].split(" ")[1])
    draws = i.split(":")[1].split(";")

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
                    cubes[key] = val
             
    p = cubes["b"] * cubes["g"] * cubes["r"]
    s += p
print(s)
