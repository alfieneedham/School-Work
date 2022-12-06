amount1 = (input())
amount2 = (input())

possibleAmounts = []

if int(amount1) <= 20:
    if len(str(amount2)) == 1:
        amount2Formatted = ("0" + str(amount2))
    else:
        amount2Formatted = amount2
    possibleAmounts.append("£" + str(amount1) + "." + str(amount2Formatted))

if int(amount2) <= 20:
    if len(str(amount1)) == 1:
        amount1Formatted = ("0" + str(amount1))
    else:
        amount1Formatted = amount1
    possibleAmounts.append("£" + str(amount2) + "." + str(amount1Formatted))

for line in range(len(possibleAmounts)):
    print(possibleAmounts[line])