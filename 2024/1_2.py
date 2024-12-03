with open('input.txt') as f:
    c = f.readlines()

left = []
right = []
for i in c:
    splitted = i.split("   ")
    left.append(int(splitted[0]))
    right.append(int(splitted[1][:-1]))

sum = 0

for i in range(len(left)):
    for j in range(len(right)):
        if left[i] == right[j]:
            sum += left[i]

print(sum)
