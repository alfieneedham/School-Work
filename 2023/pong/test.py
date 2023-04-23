import operator
operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}   

inputOp = input("")
op = operators[inputOp]
print(str(op(2, 3)))