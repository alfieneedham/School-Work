import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.clock import Clock
import random

numImages = 7
difficulty = input("Choose difficulty (easy/medium/hard): ")
displayTimes = {"easy": 1, "medium": 0.75, "hard": 0.5, "supereasy": 0}
columnSizes = {"easy": 3, "medium": 5, "hard": 7, "supereasy": 25}
displayTime = displayTimes[difficulty]
columnSize = columnSizes[difficulty]
userCanClick = True
sequenceOfButtons = []
currentSequence = []
currentUserSequence = []
allButtons = []

def iterate_turn(delta):
    global userCanClick
    global currentUserSequence
    userCanClick = False
    buttonToAdd = random.choice(allButtons)
    currentSequence.append(buttonToAdd.buttonID)
    sequenceOfButtons.append(buttonToAdd)
    allButtons.remove(buttonToAdd)
    currentUserSequence = []
    display_sequence()
    
def game_over(delta):
    print(str(1/0))
    
def check_sequence(delta):
    if currentUserSequence == currentSequence:
        for button in sequenceOfButtons:
            button.display_correct()
        if len(currentSequence) == columnSize ** 2:
            Clock.schedule_once(game_over, 1)
        else:
            Clock.schedule_once(iterate_turn, 1.5)
    else:
        for button in sequenceOfButtons:
            button.display_incorrect()
    
def handle_click(instance):
    global userCanClick
    if userCanClick == True:
        instance.parent.button_has_been_clicked()
        
def display_sequence():
    global userCanClick
    waitTime = 0
    for button in sequenceOfButtons:
        Clock.schedule_once(button.display_and_hide, waitTime)
        waitTime += displayTime   
    userCanClick = True
        
class cell(BoxLayout):
    def __init__(self, buttonID):
        super().__init__()
        self.buttonID = buttonID
        imageLocation = "buttons/button{0}.png".format(random.randrange(1, numImages + 1))
        self.imageDisplay = Image(source = imageLocation)
        self.buttonDisplay = Button()
        self.incorrectImage = Image(source = "buttons/buttonIncorrect.png")
        self.correctImage = Image(source = "buttons/buttonCorrect.png")
        self.buttonDisplay.bind(on_press = handle_click)
        self.add_widget(self.buttonDisplay)
        allButtons.append(self)
        
    def display_and_hide(self, delta):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.imageDisplay)
        Clock.schedule_once(self.display_button, displayTime)
        
    def display_image(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.imageDisplay)
        
    def display_button(self, delta):
        self.remove_widget(self.imageDisplay)
        self.remove_widget(self.correctImage)
        self.remove_widget(self.incorrectImage)
        self.add_widget(self.buttonDisplay)
        
    def display_incorrect(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.incorrectImage)
        Clock.schedule_once(game_over, 1)
        
    def display_correct(self):
        self.remove_widget(self.buttonDisplay)
        self.add_widget(self.correctImage)
        Clock.schedule_once(self.display_button, 1)
        
    def button_has_been_clicked(self):
        global userCanClick
        if userCanClick == True:
            currentUserSequence.append(self.buttonID)
            Clock.schedule_once(self.display_button, 0.1)
            self.display_image()
            if len(currentUserSequence) == len(currentSequence):
                Clock.schedule_once(check_sequence, 0.5)
        
class Application(App):
    def build(self):
        Clock.schedule_once(iterate_turn, 3)
        buttonid = 1
        layout = GridLayout(cols = columnSize)
        for x in range(columnSize):
            for y in range(columnSize):
                layout.add_widget(cell(buttonid))
                buttonid += 1        
        return layout
    
if __name__ == "__main__":     
    myApp = Application()
    myApp.run()