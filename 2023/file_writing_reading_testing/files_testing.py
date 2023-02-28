def copy_text_file(fileToOpen):
    file = str("file_writing_reading_testing/{}.txt".format(fileToOpen))
    f = open(file, "r")
    copiedFile = file + "_copy"
    newF = open(copiedFile, "w")
    newF.write(f.read())
    f.close()
    newF.close()

def generate_all_5_letter_words():

    f = open("file_writing_reading_testing/five_letter_lowercase_words.txt", "w")

    startValue = ord("a")
    endValue = ord("z")
    finished = False

    characters = {"one": ord("a"), "two": ord("a"), "three": ord("a"), "four": ord("a"), "five": ord("a")}

    while finished == False:

        word = (chr(characters["one"]) + chr(characters["two"]) + chr(characters["three"]) + chr(characters["four"]) + chr(characters["five"]) + "\n")
        
        f.write(word)

        if characters["five"] == endValue:
            characters["five"] = startValue - 1
            characters["four"] += 1
        if characters["four"] == endValue + 1:
            characters["four"] = startValue
            characters["three"] += 1
        if characters["three"] == endValue + 1:
            characters["three"] = startValue
            characters["two"] += 1
        if characters["two"] == endValue + 1:
            characters["two"] = startValue
            characters["one"] += 1
        if characters["one"] == endValue + 1:
            finished = True

        characters["five"] += 1
        

    f.close()

    
    


#fileToOpen = str(input("Enter file name: "))
#copy_text_file(fileToOpen)

generate_all_5_letter_words()