from random import randrange

numPersons = int(input("Enter number of persons: "))

probability = 1
for i in range(365, 365-numPersons, -1):
    probability *= i/365
probability = 1 - probability
print("Loop:", str(probability))

count = 0
for x in range(1000000):
    numbers = []
    for y in range(numPersons):
        numToAppend = randrange(1, 366)
        if numToAppend in numbers:
            count += 1
            break
        numbers.append(randrange(1, 366))
Mprobability = count/1000000

print("Monte Carlo:", Mprobability)
print("Difference:", str(abs(Mprobability - probability)))





"""
10: 0.1169
15: 0.2529
20: 0.4114
25: 0.5687
30: 0.7063
35: 0.8144
40: 0.8912
"""