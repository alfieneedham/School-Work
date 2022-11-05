studentData = {"John": 50, "Sarah": 36, "Fred": 40, "Mary": 30, "Luke": 49, "Harry": 51}



class ExamResults:
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def calculate_percentage(self):
        self.__examPercent = int(self.__score / 60 * 100)
        
    def calculate_grade(self):
        if self.__score >= 50:
            self.__grade = "A"
        else:
            self.__grade = "B"
            
    def calculate_data(self):
        self.calculate_percentage()
        self.calculate_grade()
            
    def calculate_and_show_student_data(self):
        self.calculate_data()
        print(self.__name + "'s results are:")
        print("Percentage: " + str(self.__examPercent))
        print("Grade: " + str(self.__grade))
        print("")
   
   
           
def create_and_display_student_results(studentData):
    
    for index in studentData:
        name = index
        score = studentData[index]
        studentResult = ExamResults(name, score)
        studentResult.calculate_and_show_student_data()

        
        
create_and_display_student_results(studentData)