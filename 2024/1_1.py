with open('input.txt') as f:
    c = f.readlines()

left = []
right = []
for i in c:
    splitted = i.split("   ")
    left.append(int(splitted[0]))
    right.append(int(splitted[1][:-1]))

left.sort()
right.sort()

sum = 0

for i in range(len(left)):
    sum += abs(left[i]-right[i])
print(sum)
