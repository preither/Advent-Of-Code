def hash(string):
    h = 0
    for i in string:
        h += ord(i)
        h *= 17
        h %= 256

    return h

with open('input.txt') as f:
    c = f.readlines()

s = 0
i = c[0][:-1].split(",")

for j in i:
    s += hash(j)


print(s)

     
