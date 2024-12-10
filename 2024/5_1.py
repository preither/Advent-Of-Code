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

cnt = 0
for u in updates:
    valid = True
    for r in rules:
        try:
            first = u.index(r[0])
            second = u.index(r[1])

            if second < first:
                valid = False
                break
        except:
            pass
    if valid:
        cnt += int(u[int((len(u))/2)])


print(cnt)