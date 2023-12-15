def check_horizontal(field):
    for i in range(len(field) - 1):
        try:
            for j in range(i+10):
                if i - j < 0 or i+j+1 > len(field) - 1:
                    return i + 1
                if field[i-j] != field[i+j+1]:
                    break
        except:
            return i + 1
    return 0

def check_vertical(field):
    new_field = []
    #transform so we could use the horizontal algorithm
    for j in range(len(field[0])):
        new_field.append("")
        for i in range(len(field)):
            new_field[j] += field[i][j]

    return check_horizontal(new_field[:-1])

with open('input.txt') as f:
    c = f.readlines()
s= 0
start = 0
for i in range(len (c)):
    if c[i] == "\n":
        s += 100 * check_horizontal(c[start:i])
        s += check_vertical(c[start:i])
        start = i + 1

s += 100* check_horizontal(c[start:])
s += check_vertical(c[start:])

print(s)