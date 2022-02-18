'''
Super Method is basically used to avoid overwriting
'''


class person:
    country = "India"

    def __init__(self):
        print("\nInitializing Person....\n")

    def takeBreak(self):
        print("I am breathing...")


class Employee(person):
    company = "Tesla"

    def __init__(self):
        super().__init__()
        print("Initializing Employee....\n")

    def getSalary(self, salary):
        self.salary = salary
        print(f"Salary is {self.salary}")

    def takeBreak(self):
        print("I am an employee so I am breathing..")


class Programmer(Employee):

    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer....\n")

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreak(self):
        super().takeBreak()  # Here this is used to print the parent class too
        print("I am a Programmer so I am breathing++")


# p=person()
# p.takeBreak()
pr = Programmer()
# e.takeBreak()


# pr.takeBreak()
