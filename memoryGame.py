import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.clock import Clock
import time
import random

numImages = 3
difficulty = input("Choose difficulty (easy/medium/hard): ")
displayTimes = {"easy": 3, "medium": 2, "hard": 1}
columnSizes = {"easy": 3, "medium": 4, "hard": 5}
numTurnsInSequence = {"easy": 3, "medium": 5, "hard": 7}
displayTime = displayTimes[difficulty]
columnSize = columnSizes[difficulty]
turnsInSequence = numTurnsInSequence[difficulty]

userCanClick = True

currentSequence = []
currentUserSequence = []

allButtons = []

def iterate_turn():
    currentSequence.append(random.randrange(1, columnSize**2 + 1))
    print(currentSequence)
    display_sequence()
    
def game_lost():
    print("hi")
    
def handle_click(instance):
    if userCanClick == True:
        instance.parent.button_has_been_clicked()
        
def display_sequence():
    for button in allButtons:
        button.display_and_hide()
        print("hi")
    

class cell(BoxLayout):
    def __init__(self, buttonID):
        super().__init__()
        self.buttonID = buttonID
        imageLocation = "buttons/button{0}.png".format(random.randrange(1, numImages + 1))
        self.imageDisplay = Image(source = imageLocation)
        self.buttonDisplay = Button()
        self.incorrectImage = Image(source = "buttons/button1.png")
        self.correctImage = Image(source = "buttons/button3.png")
        self.buttonDisplay.bind(on_press = handle_click)
        self.add_widget(self.buttonDisplay)
        allButtons.append(self)
        
    def display_and_hide(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.imageDisplay)
        Clock.schedule_once(self.display_button, displayTime)
        
    def display_image(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.imageDisplay)
        
    def display_button(self, delta):
        self.remove_widget(self.imageDisplay)
        self.add_widget(self.buttonDisplay)
        
    def display_incorrect(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.incorrectImage)
        Clock.schedule_once(game_lost, 1)
        
    def display_correct(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.correctImage)
        Clock.schedule_once(self.display_button, 1)
        
    def button_has_been_clicked(self):
        currentUserSequence.append(self.buttonID)
        Clock.schedule_once(self.display_button, 1)
        self.display_image()
        print(currentSequence)
        print(currentUserSequence)
        if len(currentUserSequence) == len(currentSequence):
            print(currentSequence)
            print(currentUserSequence)
            if currentUserSequence == currentSequence:
                print("hi")
                for x in range(columnSize):
                    for y in (columnSize):
                        self.display_correct
                numTurnsInSequence = iterate_turn(numTurnsInSequence)
            else:
                game_lost()
        

       
        
class Application(App):
    def build(self):
        buttonid = 1
        layout = GridLayout(cols = columnSize)
        for x in range(columnSize):
            for y in range(columnSize):
                layout.add_widget(cell(buttonid))
                buttonid += 1
        return layout
    iterate_turn() 
    
if __name__ == "__main__":     
    myApp = Application()
    myApp.run()