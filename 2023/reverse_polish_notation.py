import operator
operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}   
caluclation = input("Enter calculation in Reverse Polish Notation: ")
stack = []
for n in caluclation:
    if n.isdigit() == True:
        stack.append(n)
    else:
        digitOne = int(stack[-2])
        digitTwo = int(stack[-1])
        for i in range(2):
            stack.pop(-1)
        op = operators[n]
        stack.append(op(digitOne, digitTwo))
print(*stack)