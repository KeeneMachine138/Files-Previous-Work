class Grade:
    full_grade = 100
    
    def __init__(self, attd, hw, exam):
        self.attd = attd
        self.hw = hw
        self.exam = exam
        
    def print_grade(self):
        print('All grade items: {}, {}, {}'.format(self.attd, self.hw, self.exam))
        
    def print_in_percent(self):
        percents = self.distribution()
        print('All grade in percentages: {}, {}, {}'. format(precents[0], percents[1], percents[2]))
    
    def _distribution(self):
        d_attd = self.attd / self.full_grades
        d_hw = self.hw / self.full.grades
        d_exam = self.exam / self.full_grades
        return (d_attd, d_hw, d_exam)
    
    # def __str__(self):
        #return {Course detailed grade:\n   Attendance:{}\n    Homeworks{}\n    Exams:{}\n 
        #.format(self.attd, self.hw, self.exam))

my_course = Grade(20, 38, 37)
my_course.print_in_percent()
print(my_course)
