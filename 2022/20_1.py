f = open('input.txt', 'r')
lines = f.readlines()

init_array = []
shift_array = []

for l in lines:
    val = int(l[:-1])
    while val in init_array:
        val += 50000
    init_array.append(val)
    shift_array.append(val)


for i in init_array:
    index = shift_array.index(i)

    normed_value = i

    while normed_value > 10000:
        normed_value -= 50000

    new_index = (index + normed_value) % (len(init_array) - 1)

    shift_array.remove(i)
    shift_array.insert(new_index, i)



index_1000 = (shift_array.index(0) + 1000) % len(init_array)
index_2000 = (shift_array.index(0) + 2000) % len(init_array)
index_3000 = (shift_array.index(0) + 3000) % len(init_array)

val_1000 = shift_array[index_1000]
while val_1000 > 10000:
    val_1000 -= 50000

val_2000  = shift_array[index_2000]
while val_2000 > 10000:
    val_2000 -= 50000

val_3000  = shift_array[index_3000]
while val_3000 > 10000:
    val_3000 -= 50000


print(val_1000 + val_2000 + val_3000)




