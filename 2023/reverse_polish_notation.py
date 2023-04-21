import operator
operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}   






caluclation = input("Enter calculation in Reverse Polish Notation: ")
stack = []
for n in caluclation:
    if n.isdigit() == True:
        stack.append(n)
    else:
        digitOne = stack[-2]
        digitTwo=stack[-1]
        stack.pop(-1)
        stack.pop(-1)
        op = operators[n]
        print(op(digitOne, digitTwo))
