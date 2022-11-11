for i in range(3):
    print("")

class Person:
    
  _ID = 1

    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__ID = Person._ID
        Person._ID += 1
        
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

    def show_person_name(self):
        print(self.__name)
        print("")



class GroupOfPersons:

    def __init__(self):
        self.__dictionaryOfPersons = {}

    def get_and_display_group_size(self):
        groupSize = len(self.__dictionaryOfPersons)
        print("There are", str(groupSize), "persons in this group.")
        print("")
        return (groupSize)

    def create_persons(self):        
        addPersons = "y"
        while addPersons == "y":
            name = input("Enter name: ").title()
            address = input("Enter address: ").lower()
            age = input("Enter age: ")
            self.__dictionaryOfPersons[name] = Person(name, address, age)
            print("")
            addPersons = input("Add another person? (y/n) ").lower()
            print("")
        
    def display_all_persons_details(self):
        print("Details of all persons are listed below: \n")  
        for index in self.__dictionaryOfPersons:
            self.__dictionaryOfPersons[index].show_person_details()
        print("")
            
    def display_single_person_details(self):
        person = input("Please enter persons name: ").title()
        print("")
        self.dictionaryOfPersons[person].show_person_details()
        print("")
        
    def display_all_persons(self):
        print("All persons are listed below: \n")
        for index in self.__dictionaryOfPersons:
            self.__dictionaryOfPersons[index].show_person_name()
        print("")
        
    def edit_details(self):
        person = input("Enter person to edit: ").title()
        personsObjects[person].edit_person_details()
        
    def find_person_id(self):
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
        
    def find_object_with_id(self):
        idOfPersonToFind = int(input("Enter the ID of the person: "))
        personToFind = personsList[idOfPersonToFind]
        print("")
        return (personToFind)

    def display_single_persons_details_using_id(self, personID):
        personsObjects[personID].show_person_details()
        print("")
        
    def edit_single_persons_details_using_id(self, personID):
        personsObjects[personID].edit_person_details()
        print("")
        
def display_options():
    print("Please enter which option you wish to select below: \n")
    print("1. Display number of persons in group.")
    print("2. Create person(s).")
    print("3. List persons.")
    print("4. Display details of a person.")
    print("5. Display details of all persons.")
    print("6. Edit details of a person.")
    print("7. Find person ID.")
    print("8. Display details of a person by ID.")
    print("9. Edit details of a person by ID.")
    print("10. Exit program.")
    print("")

       
    
def main():
    option = "0"
    while option != "10":
        if option == "0" or option == "[0]":
            display_options()  
        if option != "0":  
            print("Enter [0] to display options.")    
        option = input("Enter option: ").lower()
        print("")
        if option == "1":
            mainGroup.get_and_display_group_size()
        if option == "2":
            mainGroup.create_persons()
        if option == "3":
            mainGroup.display_all_persons()
        if option == "4":
            mainGroup.display_all_persons()
            mainGroup.display_single_person_details()
        if option == "5":
            mainGroup.display_all_persons_details()
        if option == "6":
            mainGroup.display_all_persons_details()
            mainGroup.edit_details()
        if option == "7":
            print(str(mainGroup.find_person_id()))
        if option == "8":
            mainGroup.personID = find_object_with_id()
            mainGroup.display_single_persons_details_using_id(personID)
        if option == "9":
            mainGroup.personID = find_object_with_id()
            mainGroup.edit_single_persons_details_using_id(personID)

mainGroup = GroupOfPersons()
main()