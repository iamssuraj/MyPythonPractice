class person:
    country="India"
    def takeBreak(self):
        print("I am breathing...")
class Employee(person):
    company="Tesla"
    country="Canada"
    def getSalary(self,salary):
        self.salary=salary
        print(f"Salary is {self.salary}")
    def takeBreak(self):
        print("I am an employee so I am breathing..")
class Programmer(Employee):
    company="Fiverr"
    country = "USA"
    def getSalary(self):
        print(f"No salary to programmers")
    def takeBreak(self):
        print("I am a Programmer so I am breathing++")
p=person()
e=Employee()
pr=Programmer()
# e.getSalary(20000)
# pr.takeBreak()
print(pr.country)
print(e.country)
print(p.country)