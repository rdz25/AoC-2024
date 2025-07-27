class Computer:
    def __init__(self,A,B,C,program):
        self.combo_operands = {4:A,5:B,6:C}   # the combo operands hold registers A, B, C as ints
        self.program = program
        self.pointer = 0
        self.output = []
        self.code_map = {
            0:self.adv,
            1:self.bxl,
            2:self.bst,
            3:self.jnz,
            4:self.bxc, #
            5:self.out,
            6:self.bdv, #
            7:self.cdv #
            }
    
    def run(self):
        '''operand and opcode is int'''
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1] # oob?
            self.code_map[opcode](operand)
        # print(self.output)
    
    def printState(self):
        A = self.combo_operands[4]
        B = self.combo_operands[5]
        C = self.combo_operands[6]
        print(f"A:{A}\nB:{B}\nC:{C}")
        print(self.output)

    def getOperandValue(self, operand:int) -> int:
        if operand in self.combo_operands:
            operand = self.combo_operands[operand]
        return operand

    def adv(self,operand):
        op = self.getOperandValue(operand)
        # set A with combo
        self.combo_operands[4] //= 2**op
        self.pointer += 2        

    def bxl(self,operand):
        # op = self.getOperandValue(operand)
        # set B with literal
        self.combo_operands[5] ^= operand
        self.pointer += 2  

    def bst(self,operand):
        op = self.getOperandValue(operand)
        # set B with combo
        self.combo_operands[5] = op % 8
        self.pointer += 2  

    def jnz(self,operand):
        if self.combo_operands[4] != 0:
            #literal jump
            self.pointer = operand
        else:
            self.pointer += 2

    def bxc(self,operand):
        self.combo_operands[5] ^= self.combo_operands[6]
        self.pointer += 2

    def out(self,operand):
        op = self.getOperandValue(operand)
        self.output.append(op % 8)
        self.pointer += 2

    def bdv(self,operand):
        op = self.getOperandValue(operand)
        # set B with combo
        self.combo_operands[5] = self.combo_operands[4] // 2**op
        self.pointer += 2   

    def cdv(self,operand):
        op = self.getOperandValue(operand)
        # set C with combo
        self.combo_operands[6] = self.combo_operands[4] // 2**op
        self.pointer += 2   


# tests = []
# tests_out = []
#test 1
# test = {"A":0,"B":0,"C":9,"program":[2,6]}
# test_out = {"A":0,"B":1,"C":9,"output":[]}

#test 2
# test = {"A":10,"B":0,"C":0,"program":[5,0,5,1,5,4]}

#test 3
# test = {"A":2024,"B":0,"C":0,"program":[0,1,5,4,3,0]}

#test 4
# test = {"A":0,"B":29,"C":0,"program":[1,7]}

#test 5
# test = {"A":0,"B":2024,"C":43690,"program":[4,0]}

#big test
test = {"A":729,"B":0,"C":0,"program":[0,1,5,4,3,0]}

#getoperand test
# test = {"A":11,"B":12,"C":13,"program":[4,0]}
# a = Computer(**test)
# print(a.getOperandValue(0))
# print(a.getOperandValue(5))
# print(a.getOperandValue(6))

# a = Computer(**test)
# a.run()
# a.printState()


#input
with open('input.txt') as file:
    A = file.readline().replace('\n','')
    B = file.readline().replace('\n','')
    C = file.readline().replace('\n','')
    program = file.readline().split(',')
    prob_input = {"A":int(A),"B":int(B),"C":int(C),"program":list(map(int,program))}

a = Computer(**prob_input)
a.run()
a.printState()

