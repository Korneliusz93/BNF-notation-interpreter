class Variable():
    def __init__(self,name,value):
        self.name = name
        self.value = value

A = Variable('A',0)
B = Variable('B',0)
C = Variable('C',0)
D = Variable('D',0)
E = Variable('E',0)

variables = [A,B,C,D,E]
def calculate(text,char,variables):
    tokens = raw_input[2:].split(char)
    if tokens[0].isdigit():
        token1 = int(tokens[0])
    else:
        for v in variables:
            if v.name == tokens[0]:
                token1=v.value
    if tokens[1].isdigit():
        token2 = int(tokens[1])
    else:
        for v in variables:
            if v.name == tokens[1]:
                token2=v.value
    if char == '*': var.value = token1*token2
    if char == '+': var.value = token1+token2
    if char == '-': var.value = token1-token2
    result = var.value
    print(var.name,'=',var.value)
    return result

def assign(char,variables):
    if char.isdigit():
        token = int(char)
    else:
        for v in variables:
            if v.name == char:
                token=v.value
    result = token
    return result
        
raw_input = ''
while raw_input != 'STOP':
    raw_input = input('@ ')
    if raw_input[0] not in 'ABCDE':
        print(f'NameError: {raw_input[0]} name is forbidden.')
    else:
        for v in variables:
            if v.name is raw_input[0]:
                var=v
        if '*' in raw_input[2:]: var = calculate(raw_input[2:],'*',variables)
        elif '-' in raw_input[2:]: var = calculate(raw_input[2:],'-',variables)
        elif '+' in raw_input[2:]: var = calculate(raw_input[2:],'+',variables)
        else:
            for v in variables:
                if v.name is raw_input[0]:
                    var=v
            var.value=assign(raw_input[2:],variables)

