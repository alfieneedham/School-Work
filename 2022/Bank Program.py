from datetime import date

users = {}
standardActions = ["1. Change name", "2. Display balance", "3. Deposit", "4. Display info", ""]
goldActions = ["1. Change name", "2. Display balance", "3. Deposit", "4. Display info", "5. Add interest", "6. Withdraw", ""]

class BankAccount:   
    def __init__(self, name, address, balance):
        self.__name = name.title()
        self.__address = address
        self.__balance = balance   
        self.__type = "Standard"   
    def change_name(self, newName):
        users[self.__name] = newName
        self.__name = newName       
    def get_current_balance(self):
        print(self.__balance)   
    def deposit_amount(self, amount):
        self.__balance += amount       
    def display_account_details(self):
        print("Name: " + self.__name)
        print("Address: " + self.__address)
        print("Account type: " + self.__type)
    def get_account_type(self):
        return(self.__type)
               
class GoldBankAccount(BankAccount):   
    def __init__(self, name, address, balance, interest, date):
        self.__name = name.title()
        self.__address = address
        self.__balance = balance
        self.__interestRate = interest
        self.__dateCreated = date  
        self.__type = "Gold"     
    def add_interest(self):
        self.__balance *= self.__interestRate       
    def withdraw_money(self, amount):
        self.__balance -= amount      
    def display_account_details(self):
        print("Name: " + self.__name)
        print("Address: " + self.__address)
        print("Interest: " + self.__interestRate)
        print("Account creation date: " + str(self.__dateCreated))
        print("Account type: " + self.__type)
    def get_account_type(self):
        return(self.__type)


def intialise_accounts():               
    continueInitialiseAccounts = "y"
    while continueInitialiseAccounts == "y":       
        name = input("Name: ").title()
        address = input("Address: ")
        balance = input("Deposit: ")   
        if int(balance) >= 500:
            accountType = "gold"
        else:
            accountType = "standard"  
        if accountType.lower() == "gold":       
            interest = input("Interest: ")
            currentDate = date.today()     
            users[name] = GoldBankAccount(name, address, balance, interest, currentDate)     
        else:     
            users[name] = BankAccount(name, address, balance)      
            
        print("")
        print("The details of this account are:")            
        users[name].display_account_details()
        print("")    
        continueInitialiseAccounts = input("Do you wish to add another account? (y/n) ").lower()
        print("")
        
    
        
intialise_accounts()
       
continuePerformActions = input("Do you wish to perform actions on an account? (y/n) ").lower()
while continuePerformActions == "y":    
    print("Account names are listed here:")   
    for index in users:
        print(index)      
    account = input("Which account do you want to access? ").title()
    print("")   
    accountType = (users[account].get_account_type())  
    if accountType == "standard":
        for index in range(len(standardActions)):
            print(standardActions[index])
    else:
        for index in range(len(goldActions)):
            print(goldActions[index])
            
    action = input("Enter the action you want to perform (enter the nunmerical value) ")
    
    if action == "1":
        newName = input("Enter the new name: ")
        users[account].change_name(newName)
            
                  
    continuePerformActions = input("Do you wish to perform another action? (y/n) ").lower()