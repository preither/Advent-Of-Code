with open('input.txt') as f:
    c = f.readlines()



s = 0
for j in range(len(c[0])):
    val = len(c)
    for i in range(len (c)):
        shape = c[i][j]

        if shape == "#":
            val = len(c) - i - 1

        if shape == "O":
            s += val
            val -= 1

print(s)

     
