pieces = {
    "|": {"U": [-1,0,"U"], "O": [1,0,"O"]},
    "-": {"L": [0, 1,"L"], "R": [0,-1,"R"]},
    "L": {"O": [0, 1,"L"], "R": [-1,0,"U"]},
    "J": {"L": [-1, 0,"U"], "O": [0,-1,"R"]},
    "7": {"L": [1, 0,"O"], "U": [0,-1,"R"]},
    "F": {"U": [0, 1,"L"], "R": [1,0,"O"]},    

}

with open('input.txt') as f:
    c = f.readlines()

field = []
pos = [0,0]
for i in range(len(c)):
    field.append([])
    for j in range(len(c[0])-1):
        field[i].append(c[i][j])
        if c[i][j] == "S":
            pos = [i,j]

cnt = 0
step = [0,1,"L"]

while True:
    pos[0] += step[0]
    pos[1] += step[1]

    next_field = field[pos[0]][pos[1]]
    cnt += 1
    try:
        next_step = pieces[next_field][step[2]]
    except:
        print(next_field)
        break

    step = next_step

print(cnt/2)




