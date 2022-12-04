import random

amountNumbersToUse = 5

numbers = [1, 5, 10, 15, 20, 30, 40, 50, 75, 100, 200, 250, 500]
numbersInUse = []
operations = ["+", "-", "*"]

def obtain_numbers_to_use():

    for index in range(amountNumbersToUse):
        getNumber = True
        while getNumber == True:
            numberToAddPosition = random.randrange(0, len(numbers))
            numberToAdd = numbers[numberToAddPosition]
            if numberToAdd in numbersInUse:
                pass
            else:
                numbersInUse.append(numberToAdd)
                getNumber = False
                
def generate_number():

    operation1 = random.choice(operations)
    operation2 = random.choice(operations)
    num1 = random.choice(numbersInUse)
    num2 = random.choice(numbersInUse)
    num3 = random.choice(numbersInUse)
    
    print(str(operation1))
    print(str(operation2))
    print(str(num1))
    print(str(num2))
    print(str(num3))
    
    if operation1 == "+":
        resultPartA = num1 + num2
    if operation1 == "-":
        resultPartA = num1 - num2
    if operation1 == "*":
        resultPartA = num1 * num2    
    if operation2 == "+":
        resultPartB = resultPartA + num3
    if operation2 == "-":
        resultPartB = resultPartA - num3
    if operation2 == "*":
        resultPartB = resultPartA * num3
              
    print(str(resultPartB))
    
    
 
obtain_numbers_to_use()
generate_number()
 
numbersInUse.sort()          
#for index in range(len(numbersInUse)):
 #   print (str(numbersInUse[index]))