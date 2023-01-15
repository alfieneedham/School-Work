dictOfNumerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

# * Obtains the number in Roman Numerals that the user inputs and checks its format:
def obtain_num_in_numerals():   
    obtainAnInput = True
    while obtainAnInput == True:
        numInNumerals = (input("Enter the number in Roman Numerals here: ").upper())
        if len(numInNumerals) != 0:
            obtainAnInput = False
            for index in range(len(numInNumerals)):
                if numInNumerals[index] not in dictOfNumerals:
                    obtainAnInput = True
    return(numInNumerals)
    
# * converts the Roman Numerals to denary:
def find_num_in_denary(numeralNum):
    
    listOfNumerals = []
    for index in range(len(numeralNum)):
        listOfNumerals.append(numeralNum[index])
        
    total = 0
    while True:
        
        if len(listOfNumerals) >= 2:
            if dictOfNumerals[listOfNumerals[1]] > dictOfNumerals[listOfNumerals[0]]:
                total += (dictOfNumerals[listOfNumerals[1]] - dictOfNumerals[listOfNumerals[0]])
                del listOfNumerals[0]
                del listOfNumerals[0]
                
            else:
                total += dictOfNumerals[listOfNumerals[0]]
                del listOfNumerals[0]
    
        elif len(listOfNumerals) == 1:
            total += dictOfNumerals[listOfNumerals[0]]
            del listOfNumerals[0]
            
        else:
            return(total)
 
# * Outputs the Roman Numeral:       
def output_the_numeral(numeral):
    print("This number in denary is:", numeral)
   
if __name__ == "__main__":
    numberInRomanNumerals = obtain_num_in_numerals()
    numberInDenary = find_num_in_denary(numberInRomanNumerals)
    output_the_numeral(numberInDenary)