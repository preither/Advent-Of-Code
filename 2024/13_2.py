with open('input.txt') as f:
    contents = f.read()

blocks = contents.split("\n\n")

costA = 3
costB = 1
prize_add = 10000000000000

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
    p = (int(Prize[1][2:-1]) + prize_add, (int(Prize[2][2:])) + prize_add)
    
    
    # Gleichungssystem
    # I : a * x_a + b * x_b = x_p
    # II: a * y_a + b * y_b = y_p
    #
    # I nachb : b = (x_p/x_b) - (x_a/x_b) * a
    # a in II:  a_z = y_p - (x_p * y_b) / x_b
    #           a_n = y_a - (x_a * y_b) / x_b
    a_z = p[0] - ((p[1] * b[0])/b[1])
    a_n = a[0] - ((a[1] * b[0])/b[1])

    a_cnt = round(a_z / a_n)
    b_cnt = round((p[1] / b[1]) - ((a[1]/b[1]) * a_cnt))

    #check if values realy match
    if a_cnt * a[1] + b_cnt * b[1] == p[1] and a_cnt * a[0] + b_cnt * b[0] == p[0]:
        tokens += a_cnt * costA + b_cnt * costB

print(tokens)