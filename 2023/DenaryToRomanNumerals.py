dictOfNumerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4,"I": 1}

# * Obtains the denary number that the user inputs and checks its format:
def obtain_denary_num():   
    while True:
        try:
            denaryNum = int(input("Enter the number in Roman Numerals: "))
            if denaryNum > 0:
                return(denaryNum)
        except:
            pass
    
# * Finds the number in Roman Numerals:
def find_largest_numeral(denaryNum):
    numeralNum = ""
    while True:   
        for numeral in dictOfNumerals:
            if dictOfNumerals[numeral] == denaryNum:
                numeralNum += numeral
                return (numeralNum)
            elif dictOfNumerals[numeral] < denaryNum:
                denaryNum -= dictOfNumerals[numeral]
                numeralNum += numeral
                break
 
# * Outputs the Roman Numeral:       
def output_the_numeral(numeral):
    print("This number in Roman Numerals is:", numeral)
       
if __name__ == "__main__":
    numInDenary = obtain_denary_num()
    numInNumerals = find_largest_numeral(numInDenary)
    output_the_numeral(numInNumerals)