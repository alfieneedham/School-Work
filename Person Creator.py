class Person:
    
    def __init__(self):
        self.__name = ""
        self.__address = ""
        self.__age = 0
        
    def add_person_details(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age
        
    def edit_person_details(self, option):
        if option == "1":
            newName = input("Enter new name: ")
            self.__name = newName
        if option == "2":
            newAddress = input("Enter new address: ")
            self.__address = newAddress
        if option == "3":
            newAge = input("Enter new age: ")
            self.__age = newAge
        print("")
            
    def show_person_details(self):
        print("Person details:")
        print("Name: " + self.__name)
        print("Address: " + self.__address)
        print("Age: " + self.__age)
        