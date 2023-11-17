import operator
operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}   
caluclation = input("Enter calculation in Reverse Polish Notation: ")
stack = []
for char in caluclation:
    if char.isdigit():
        stack.append(char)
    else:
        digitOne = int(stack[-2])
        digitTwo = int(stack[-1])
        for i in range(2):
            stack.pop(-1)
        op = operators[char]
        stack.append(op(digitOne, digitTwo))
print(*stack)