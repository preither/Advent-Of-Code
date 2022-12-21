import sympy as sy
h_key = "humn"
class Num:
    def __init__(self, name, operation):
        self.name = name
        self.operation = operation
        if name == "root":
            self.operation = operation.replace("+", "==")
        self.observer = []
        self.val = ""
        pass

    def add_observer(self, observer):
        self.observer.append(observer)

    def set_value(self, val):
        self.val = str(val)
        for ob in self.observer:
            ob.notify(self.name, self.val)

    def notify(self, name, val):
        self.operation = self.operation.replace(name, val)
        try:
            if h_key in self.operation:
                try:
                    humn = 1
                    eval(self.operation)
                    self.set_value("(" + self.operation + ")")
                except:
                    pass
            else:
                self.set_value(eval(self.operation))
        except:
            pass

f = open('input.txt', 'r')
lines = f.readlines()

dic = {}

for l in lines:
    cut = l[:-1].split(": ")
    dic[cut[0]] = Num(cut[0], cut[1])

for key in dic:
    obj = dic[key]
    if not obj.operation.isnumeric():
        cut = obj.operation.split(" ")

        dic[cut[0]].add_observer(obj)
        dic[cut[2]].add_observer(obj)

for key in dic:
    obj = dic[key]
    if obj.operation.isnumeric():
        if key == h_key:
            obj.set_value(h_key)
        else:
            obj.set_value(obj.operation)

cut = dic["root"].val.split(" == ")

humn = sy.S('humn')
a = sy.Eq(sy.sympify(cut[0][1:]), sy.sympify(cut[1][:-1]))

print(sy.solve(a))
