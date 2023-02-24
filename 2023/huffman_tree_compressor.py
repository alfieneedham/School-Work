text = str(input("Enter text to compress here: "))

dictOfCharacters = {}
dictOfHuffmanCodes = {}
huffmanCode = ""

# * Function that returns the smallest occurring character and its number of occurrences, after deleting that character from the dictionary.
def find_smallest_occurrence():
    minimumValue = (min(dictOfCharacters.values()))
    for char in dictOfCharacters:
        if dictOfCharacters[char] == minimumValue:
            smallestChar = char
            value = dictOfCharacters[char]
            dictOfCharacters.pop(char)
            return(smallestChar, value)

# * Each character in text become a key. The number of occurences is the value.
for char in range(len(text)):
    if text[char] in dictOfCharacters:
        dictOfCharacters[text[char]] += 1
    else:
        dictOfCharacters[text[char]] = 1

# * Adds the characters to the huffman dictionary, assigning them a value of 0 or 1. The final combination is given a value of None.
while len(dictOfCharacters) > 1:   
    value1 = 0
    value2 = 0
    smallestChar1 = ""
    smallestChar2 = ""
    smallestChar1, value1 = ((find_smallest_occurrence()))
    smallestChar2, value2 = ((find_smallest_occurrence()))    
    dictOfHuffmanCodes[smallestChar1] = (smallestChar1 + smallestChar2, 0)
    dictOfHuffmanCodes[smallestChar2] = (smallestChar1 + smallestChar2, 1)
    dictOfCharacters[smallestChar1 + smallestChar2] = value1 + value2   
for char in dictOfCharacters:
    dictOfHuffmanCodes[char] = None

print(dictOfHuffmanCodes)

def create_huffman_code(char):
    print(char)
    if dictOfHuffmanCodes[char] is None:
        return("")
    return(create_huffman_code(dictOfHuffmanCodes[char][0]) + str(dictOfHuffmanCodes[char][1]))
    
for i in range(len(text)):
    huffmanCode += create_huffman_code(text[i])

print(str(huffmanCode))