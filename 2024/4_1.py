def check_field(content, x, y, x_dir, y_dir):
    if content[y][x] != "X":
        return 0
    
    word = ["M", "A", "S"]
    for i in range (3):
        x += x_dir
        y += y_dir

        if x < 0 or y < 0 or y >= len(content) or x >= len(content[0]) - 1:
            return 0
        
        if content[y][x] != word[i]:
            return 0

    return 1


with open('input.txt') as f:
    c = f.readlines()

cnt = 0
for y in range(len(c)):
    for x in range(len(c[0])):
        #right
        cnt += check_field(c, x, y, 1, 0)
        #right down
        cnt += check_field(c, x, y, 1, 1)
        #down
        cnt += check_field(c, x, y, 0, 1)
        #left down
        cnt += check_field(c, x, y, -1, 1)
        #left
        cnt += check_field(c, x, y, -1, 0)
        #left up
        cnt += check_field(c, x, y, -1, -1)
        #up
        cnt += check_field(c, x, y, 0, -1)
        #right up
        cnt += check_field(c, x, y, 1, -1)

print(cnt)

