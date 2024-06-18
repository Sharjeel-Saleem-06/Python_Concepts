class person:
    name="harry"
    occupatiojn="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is {self.occupatiojn}")


a=person()
a.name="shutdown"
a.occupatiojn="dr"
print(a.name , a.occupatiojn)


# to check grade of a student
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

student = Student("Bob", 1234, 85)
print("Grade:", student.calculate_grade())


# Create a class called Employee with attributes name, designation, and salary.
#  Implement a method display_info() that prints the employee's information.
class Employee:
    def __init__(self, name, designation, salary):
        self.name=name
        self.designation=designation
        self.salary=salary
    def displayinfo(self):
        print(f"Name: {self.name}")
        print(f"Deignation: {self.designation}")
        print(f"Salary: {self.salary}")
    @staticmethod
    def greet():
        print("Hello, I am an employee")

employee=Employee("Sharjeel","Software Developer",40000)  
(employee.displayinfo())  



