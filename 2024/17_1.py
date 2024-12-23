class computer():
    a = 0
    b = 0
    c = 0
    pointer = 0
    instruction_set = []
    output = ""
    def combo_operand(self, combo):
        if combo <= 3:
            return combo
        if combo == 4:
            return self.a
        if combo == 5:
            return self.b
        if combo == 6:
            return self.c

    def perfom_instruction(self, opcode, combo):
        instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

        if instructions[opcode](combo):
            self.pointer += 2

    def adv(self, combo):
        val = self.combo_operand(combo)
        self.a = int(self.a / (1 << val))
        return True
    
    def bxl(self, combo):
        self.b = self.b ^ combo
        return True
    
    def bst(self, combo):
        val = self.combo_operand(combo)
        self.b = val % 8
        return True
    
    def jnz(self, combo):
        if self.a == 0:
            return True
        else:
            self.pointer = combo
            return False
    
    def bxc(self, combo):
        self.b = self.b ^self.c
        return True
    
    def out(self, combo):
        val = self.combo_operand(combo) % 8
        self.output += str(val) + ","
        return True
    
    def bdv(self, combo):
        val = self.combo_operand(combo)
        self.b = int(self.a / (1 << val))
        return True
    
    def cdv(self, combo):
        val = self.combo_operand(combo)
        self.c = int(self.a / (1 << val))
        return True

with open('input.txt') as f:
    contents = f.readlines()

comp = computer()

comp.a = int(contents[0][:-1].split(" ")[2])
comp.b = int(contents[1][:-1].split(" ")[2])
comp.c = int(contents[2][:-1].split(" ")[2])

comp.instruction_set = list(map(int, contents[4][:-1].split(" ")[1].split(",")))
comp.pointer = 0


while comp.pointer < len(comp.instruction_set):
    comp.perfom_instruction(comp.instruction_set[comp.pointer], comp.instruction_set[comp.pointer + 1])

print(comp.output[:-1])