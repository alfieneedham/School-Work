numCharsBorder = int(input())
numCharsFill = int(input())
borderChar = str(input())
fillChar = str(input())
gap = numCharsBorder - numCharsFill - 2
if gap != 0:
    gap /= 2

rectangle = []



line = []
for index in range(numCharsBorder):
    line.append(borderChar)
rectangle.append(line)

for x in range(numCharsFill + int(gap)):
    line = []
    line.append(borderChar)
    for i in range(int(gap)):
        line.append(" ")
    for y in range(numCharsFill):
        if x+1 <= int(gap):
            line.append(" ")
        else:
            line.append(fillChar)
    for i in range(int(gap)):
        line.append(" ")
    line.append(borderChar)
    rectangle.append(line)

if gap > int(0):
    for index in range(int(gap)):
        line = []
        line.append(borderChar)
        for i in range(int(gap)*2 + numCharsFill):
            line.append(" ")
        line.append(borderChar)
        rectangle.append(line)

line = []
for index in range(numCharsBorder):
    line.append(borderChar)
rectangle.append(line)

for line in range(len(rectangle)):
    print(*rectangle[line], sep='')