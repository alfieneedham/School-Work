from datetime import date

users = []
standardActions = ["Change name", "Display balance", "Deposit", "Display info"]
goldActions = ["Change name", "Display balance", "Deposit", "Display info", "Add interest", "Withdraw"]

class BankAccount:   
    def __init__(self, name, address, balance):
        self.__name = name.title()
        self.__address = address
        self.__balance = balance   
        self.__type = "Standard"   
    def change_name(self, newName):
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
        name = input("Name: ")
        name = name.title()
        users.append(name)
        address = input("Address: ")
        balance = input("Deposit: ")   
        if int(balance) >= 500:
            accountType = "gold"
        else:
            accountType = "standard"  
        if accountType.lower() == "gold":       
            interest = input("Interest: ")
            currentDate = date.today()     
            name = GoldBankAccount(name, address, balance, interest, currentDate)     
        else:     
            name = BankAccount(name, address, balance)      
            
        print("")
        print("The details of this account are:")            
        name.display_account_details()
        print("")    
        continueInitialiseAccounts = input("Do you wish to add another account? (y/n) ")
        
    
        
intialise_accounts()
    
continuePerformActions = "y"
while continuePerformActions == "y":
    
    print("Account names are listed here:")   
    for index in range(len(users)):
        print(users[index])       
    account = input("Which account do you want to access? ").title()
    print(account)
    
    print(account.get_account_type())
    
    if accountType == "standard":
        for index in range(len(standardActions)):
            print(standardActions[index])
    else:
        for index in range(len(goldActions)):
            print(goldActions[index])
        
    continuePerformActions = input("Do you wish to perform another action? (y/n) ")