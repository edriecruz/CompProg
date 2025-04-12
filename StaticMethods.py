class SchoolOne:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, grades):
        self.students[name] = grades
    
    @staticmethod
    def calculate_average(grades):
        return sum(grades) / len(grades)
    
    def display_averages(self):
        for name, grades in self.students.items():
            avg = self.calculate_average(grades)
            print(f"{name}: Average Grade = {avg:.2f}")

class SchoolTwo:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, credit_hours, grade_points):
        self.students[name] = (credit_hours, grade_points)
    
    @staticmethod
    def calculate_gpa(credit_hours, grade_points):
        return grade_points / credit_hours
    
    def display_gpas(self):
        for name, (credits, points) in self.students.items():
            gpa = self.calculate_gpa(credits, points)
            print(f"{name}: GPA = {gpa:.2f}")

school1 = SchoolOne()
school1.add_student("Alice", [90, 85, 92, 88])
school1.add_student("Bob", [78, 82, 80, 85])
school1.display_averages()

school2 = SchoolTwo()
school2.add_student("Charlie", 15, 45)
school2.add_student("Dana", 12, 42)
school2.display_gpas()