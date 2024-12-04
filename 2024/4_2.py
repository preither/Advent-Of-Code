def check_field(content, x, y):
    if content[y][x] != "A":
        return 0
    
    words = [["M", "M", "S", "S"], ["S", "M", "M", "S"], ["S", "S", "M", "M"], ["M", "S", "S", "M"]]
    direction = [(-1,1), (-1,-1), (1,-1), (1,1)]

    for w in words:
        for i in range (len(w)):
            x_c = x + direction[i][0]
            y_c = y + direction[i][1]

            if x_c < 0 or y_c < 0 or y_c >= len(content) or x_c >= len(content[0]) - 1:
                break
            
            if content[y_c][x_c] != w[i]:
                break

            if i == len(w)-1:
                return 1

    return 0


with open('input.txt') as f:
    c = f.readlines()

cnt = 0
for y in range(len(c)):
    for x in range(len(c[0])):
        #right
        cnt += check_field(c, x, y)

print(cnt)

