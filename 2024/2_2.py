def test(array): 
    increasing = False
    if array[0] < array[1]:
        increasing = True
    
    for i in range(len(array)): 
        if i == len(array) -1:
            return 1
        
        if increasing:
            if array[i] > array[i+1]:
                return 0
        else:
            if array[i] < array[i+1]:
                return 0
        dif = abs(array[i] - array[i+1])
        if dif < 1 or dif > 3:
            return 0 

with open('input1.txt') as f:
    contents = f.readlines()

cnt = 0
for j in contents:
    arr = []
    spl = j[:-1].split(" ")
    for i in spl:
        arr.append(int(i))

    score = test(arr)

    if score == 0:
        for i in range(len(arr)):
            new_arr = arr[:i]
            new_arr.extend(arr[i+1:])
            if test(new_arr) != 0:
                score = 1
                break

    cnt += score

print(cnt)
