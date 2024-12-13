with open('input.txt') as f:
    contents = f.read()

blocks = contents.split("\n\n")

costA = 3
costB = 1

tokens = 0

for b in blocks:
    if len(b) == 0:
        continue
    lines = b.split("\n")

    #get A
    ButtonA = lines[0].split(" ")
    a = (int(ButtonA[2][2:-1]), (int(ButtonA[3][2:])))

    #get B
    ButtonB= lines[1].split(" ")
    b = (int(ButtonB[2][2:-1]), (int(ButtonB[3][2:])))

    #get Prize
    Prize= lines[2].split(" ")
    p = (int(Prize[1][2:-1]), (int(Prize[2][2:])))


    for a_cnt in range(100):
        restX = p[0] - a_cnt*a[0]

        if restX < 0:
            break

        if restX % b[0] == 0:
            b_cnt = int(restX/b[0])
            if a_cnt * a[1] + b_cnt * b[1] == p[1]:
                #found it
                tokens += a_cnt * costA + b_cnt * costB
                break

print(tokens)