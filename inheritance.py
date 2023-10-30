class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname



class Student(Person):
    def __init__(self, fname, lname, id, testScores):
        super().__init__(fname, lname)
        self.id = id
        self.testScores = testScores
    
    def calculateGrade() -> chr:
        sum = 0.00
        for grade in self.testScores:
            sum += grade
        
        avg = sum / len(self.testScores)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

kmoore = Student("Katherine", "Moore", "12345", [80, 95, 76, 88])