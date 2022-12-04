import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import random

numbers = [1, 5, 10, 15, 20, 30, 40, 50, 75, 100, 200, 250, 500]
numbersInUse = []
operations = ["+", "-", "*"]

def obtain_numbers_to_use():

    for index in range(5):
        getNumber = True
        while getNumber == True:
            numberToAddPosition = random.randrange(0, len(numbers))
            numberToAdd = numbers[numberToAddPosition]
            if numberToAdd in numbersInUse:
                pass
            else:
                numbersInUse.append(numberToAdd)
                getNumber = False
                
def generate_number():
    operation1 = random.choice(operations)
    operation2 = random.choice(operations)
    num1 = random.choice(numbersInUse)
    num2 = random.choice(numbersInUse)
    num3 = random.choice(numbersInUse) 
    if operation1 == "+":
        resultPartA = num1 + num2
    if operation1 == "-":
        resultPartA = num1 - num2
    if operation1 == "*":
        resultPartA = num1 * num2    
    if operation2 == "+":
        resultPartB = resultPartA + num3
    if operation2 == "-":
        resultPartB = resultPartA - num3
    if operation2 == "*":
        resultPartB = resultPartA * num3
    return(resultPartB)
    
obtain_numbers_to_use()
result = generate_number()
numbersInUse.sort()          

class Application(App):
    def build(self):
        layout = GridLayout(cols = 6)
        
        # * Label displaying result of the computer calculation.
        self.displayComputerResult = Label(text = "Number: " + str(result))
        layout.add_widget(self.displayComputerResult)
        
        # * Adds buttons that allow user to select buttons chosen.
        self.numberButtonOne = Button(text = str(numbersInUse[0]))
        #self.numberButtonOne.bind(on_press = self.add_number_one)
        layout.add_widget(self.numberButtonOne)       
        
        self.numberButtonTwo = Button(text = str(numbersInUse[1]))
        #self.numberButtonTwo.bind(on_press = self.add_number_two)
        layout.add_widget(self.numberButtonTwo)
        
        self.numberButtonThree = Button(text = str(numbersInUse[2]))
        #self.numberButtonThree.bind(on_press = self.add_number_three)
        layout.add_widget(self.numberButtonThree)
        
        self.numberButtonFour = Button(text = str(numbersInUse[3]))
        #self.numberButtonFour.bind(on_press = self.add_number_four)
        layout.add_widget(self.numberButtonFour)
        
        self.numberButtonFive = Button(text = str(numbersInUse[4]))
        #self.numberButtonFive.bind(on_press = self.add_number_five)
        layout.add_widget(self.numberButtonFive)
        
        # * Adds operations, including backspace.
        self.operationButtonAdd = Button(text = "Add")
        #self.operationButtonAdd.bind(on_press = self.operation_add)
        layout.add_widget(self.operationButtonAdd)
        
        self.operationButtonSub = Button(text = "Sub")
        #self.operationButtonSub.bind(on_press = self.operation_sub)
        layout.add_widget(self.operationButtonSub)
        
        self.operationButtonMul = Button(text = "Mul")
        #self.operationButtonMul.bind(on_press = self.operation_mul)
        layout.add_widget(self.operationButtonMul)
        
        self.operationButtonDel = Button(text = "Del")
        #self.operationButtonDel.bind(on_press = self.operation_del)
        layout.add_widget(self.operationButtonDel)
        
        # * Adds button to calculate result of the operation.
        self.calculateResult = Button(text = "Calculate")
        #self.calculateResult.bind(on_press = self.calculate_result)
        layout.add_widget(self.calculateResult)  
        
        # * Displays window to display various information relevant at time.
        self.displayWindow = Label(text = "aaaaaaa")
        layout.add_widget(self.displayWindow)    
        
        return (layout)
    
if __name__ == "__main__":
    myApp = Application()
    myApp.run()
          