string = "abcdeabcde"
listOfCharacters = []
for index in range(len(string)):
    listOfCharacters.append(string[index])
    
del listOfCharacters[0]

print(listOfCharacters)