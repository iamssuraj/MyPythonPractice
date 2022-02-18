'''
Super Method is basically used to avoid overwriting
'''

class person:
    country="India"
    def takeBreak(self):
        print("I am breathing...")
class Employee(person):
    company="Tesla"
    def getSalary(self,salary):
        self.salary=salary
        print(f"Salary is {self.salary}")
    def takeBreak(self):
        super().takeBreak()
        print("I am an employee so I am breathing..")
class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")
    def takeBreak(self):
        super().takeBreak() #Here this is used to print the parent class too
        print("I am a Programmer so I am breathing++")
p=person()
p.takeBreak()
print("\n\n\n")
e=Employee()
e.takeBreak()
print("\n\n\n")
pr=Programmer()
pr.takeBreak()
print("\n\n\n")