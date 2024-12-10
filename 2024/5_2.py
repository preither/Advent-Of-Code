with open('input.txt') as f:
    contents = f.readlines()

cnt = 0
rules = []
updates = []

parse_rules = True
for j in contents:
   if j == "\n":
       parse_rules = False
   else:
       if parse_rules:
           rules.append(j[:-1].split("|"))
       else:
           updates.append(j[:-1].split(","))

invalid = []
for u in range(len(updates)):
    for r in rules:
        try:
            first = updates[u].index(r[0])
            second = updates[u].index(r[1])

            if second < first:
                invalid.append(u)
                break
        except:
            pass

cnt = 0
for i in invalid:
    u = updates[i][1:]

    correct_order = [updates[i][0]]

    for num in u:
        index_to_put = 0
        for r in rules:
            if r[1] == num and r[0] in correct_order:
                put_index = correct_order.index(r[0]) + 1
                if put_index > index_to_put:
                    index_to_put = put_index
        if index_to_put < len(correct_order):
            correct_order.insert(index_to_put, num)
        else:
            correct_order.append(num)

    cnt += int(correct_order[int((len(correct_order))/2)])

print(cnt)