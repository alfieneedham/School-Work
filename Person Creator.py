for i in range(3):
    print("")

personsObjects = {}
personsList = []

class Person:
    
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age
        
    def edit_person_details(self):
        continueToEditDetails = "y"
        while continueToEditDetails == "y":
            print("Options:")
            print("1. Change name.")
            print("2. Change address.")
            print("3. Change age.")
            option = input("Enter option: ")
            if option == "1":
                newName = input("Enter new name: ").title()
                self.__name = newName
                print("")
            if option == "2":
                newAddress = input("Enter new address: ").lower()
                self.__address = newAddress
                print("")
            if option == "3":
                newAge = input("Enter new age: ")
                self.__age = newAge
                print("")
            continueToEditDetails = input("Do you wish to edit another detail? (y/n) ").lower()
        print("")
            
    def show_person_details(self):
        print("Name: " + self.__name)
        print("Address: " + self.__address)
        print("Age: " + self.__age + "\n")
        print("")

def create_persons():       
    
    addPersons = "y"
    while addPersons == "y":
        name = input("Enter name: ").title()
        address = input("Enter address: ").lower()
        age = input("Enter age: ")
        personsObjects[name] = Person(name, address, age)
        personsList.append(name)
        print("")
        addPersons = input("Add another person? (y/n) ").lower()
        print("")
    
def display_all_persons_details():
    print("Details of all persons are listed below: \n")  
    for index in personsObjects:
        personsObjects[index].show_person_details()
    print("")
        
def display_single_person_details():
    person = input("Please enter persons name: ").title()
    print("")
    personsObjects[person].show_person_details()
    print("")
    
def display_all_persons():
    print("All persons are listed below: \n")
    for index in range(len(personsList)):
        print(personsList[index])
    print("")
    
def edit_details():
    person = input("Enter person to edit: ").title()
    personsObjects[person].edit_person_details()
    
def find_person_id():
    personID = -1
    person = input("Enter name to find: ").title()
    for index in range(len(personsList)):
        if personsList[index] == person:
            personID = index
    print("")
    if personID == -1:
        print("Person not found.")
    else:
        print("ID of", person, "is", str(personID))       
    print("") 
    
def find_object_with_id():
    idOfPersonToFind = int(input("Enter the ID of the person: "))
    personToFind = personsList[idOfPersonToFind]
    print("")
    return (personToFind)

def display_single_persons_details_using_id(personID):
    personsObjects[personID].show_person_details()
    print("")
    
def edit_single_persons_details_using_id(personID):
    personsObjects[personID].edit_person_details()
    print("")
        
def display_options():
    print("Please enter which option you wish to select below: \n")
    print("1. Create person(s).")
    print("2. List persons.")
    print("3. Display details of a person.")
    print("4. Display details of all persons.")
    print("5. Edit details of a person.")
    print("6. Find person ID.")
    print("7. Display details of a person by ID.")
    print("8. Edit details of a person by ID.")
    print("9. Exit program.")
    print("")
        
def main():
    option = "0"
    while option != "9":
        if option == "0" or option == "[0]":
            display_options()  
        if option != "0":  
            print("Enter [0] to display options.")    
        option = input("Enter option: ").lower()
        print("")
        if option == "1":
            create_persons()
        if option == "2":
            display_all_persons()
        if option == "3":
            display_all_persons()
            display_single_person_details()
        if option == "4":
            display_all_persons_details()
        if option == "5":
            display_all_persons_details()
            edit_details()
        if option == "6":
            print(str(find_person_id()))
        if option == "7":
            personID = find_object_with_id()
            display_single_persons_details_using_id(personID)
        if option == "8":
            personID = find_object_with_id()
            edit_single_persons_details_using_id(personID)
   
main()