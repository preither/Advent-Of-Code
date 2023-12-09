def next_row (arr):
    next = []

    for i in range(len(arr)-1):
        next.append(arr[i+1]-arr[i])

    return next

def check_zero (arr):
    zero = True

    for i in arr:
        if i != 0:
            zero = False
            break

    return zero

with open('input.txt') as f:
    c = f.readlines()

s = 0
for l in c: 
    arr = [[]]
    split = l[:-1].split(" ")
    for i in split:
        arr[0].append(int(i))

    while not check_zero(arr[-1]):
        arr.append(next_row(arr[-1]))

    cal = 0
    for i in range(len(arr)):
        cal = arr[len(arr)-1-i][-1] + cal

    s += cal

print(s)

    
    