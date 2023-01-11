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
    
# * Finds the largest numeral smaller than the inputted denary number:
def find_position_of_largest_numeral(denaryNum):

 
# * Outputs the Roman Numeral:       
def output_the_numeral(numeral):
    print("This number in Roman Numerals is:", numeral)
  
  
  
  
if __name__ == "__main__":
    numberInRomanNumerals = obtain_num_in_numerals()