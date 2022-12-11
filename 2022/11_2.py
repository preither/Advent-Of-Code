import math

class monkey():
    def __init__(self):
        self.items = []
        self.op = ""
        self.test = 0
        self.next_t = 0
        self.next_f = 0
        self.inspected = 0
divisors = []

class item:
    def __init__(self, num):
        self.rest = {}
        for d in divisors:
            self.rest[d] = num % d


f = open('input.txt', 'r')
lines = f.readlines()

monkeys =[]

for i in lines:
    cut = i[:-1].replace(",","").split(" ")
    try:
        key = cut[2]
    except:
        continue
    if key == "Test:":
        divisors.append(int(cut[5]))


for i in lines:
    cut = i[:-1].replace(",","").split(" ")
    if cut[0] == "Monkey":
        monkeys.append(monkey())
    else:
        try:
            key = cut[2]
        except:
            continue
        if key == "Starting":
            items = []
            for n in cut[4:]:
                test = item(int(n))
                items.append(test)
            monkeys[-1].items = items
        elif key == "Operation:":
            op = "".join(cut[5:])
            monkeys[-1].op = op
        elif key == "Test:":
            monkeys[-1].test = int(cut[5])
        else:
            if cut[5] == "true:":
                monkeys[-1].next_t = int(cut[9])
            else:
                monkeys[-1].next_f = int(cut[9])

rounds = 10000
for i in range (rounds):
    for m in monkeys:
        for it in m.items:
            for d in divisors:
                old = it.rest[d]
                new = eval(m.op) % d
                it.rest[d] = new

            if it.rest[m.test] == 0:
                n = m.next_t
            else:
                n = m.next_f
            monkeys[n].items.append(it)
            m.inspected += 1

        m.items = []

top = [0,0]
for m in monkeys:
    if m.inspected > top[0]:
        top[0] = m.inspected
    top.sort()

print(top[0]*top[1])