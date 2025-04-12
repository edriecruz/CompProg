class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    
    @classmethod
    def from_name_only(cls, name):
        return cls(name, None, None)
    
    @classmethod
    def from_name_and_id(cls, name, emp_id):
        return cls(name, emp_id, None)
    
    def display(self):
        return f"Employee: {self.name}, ID: {self.emp_id}, Dept: {self.department}"

emp1 = Employee("John Doe", 1001, "IT")
emp2 = Employee.from_name_only("Jane Smith")
emp3 = Employee.from_name_and_id("Bob Johnson", 1002)

print(emp1.display())
print(emp2.display())
print(emp3.display())