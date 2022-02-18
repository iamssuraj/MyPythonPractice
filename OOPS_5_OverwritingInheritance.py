# This uses dry principle
# inheritance is a way of creating new class from
# an exisiting class
class Employee:  # base class/parent class
    company = "Google"

    def details(self):
        print("This is an employee")


class programmer(Employee):  # child class/ derived class
    lang = "Python"

    def getLang(self):
        print(f"The language is {self.lang}")

    def details(self):
        print("This is an edited employee")


# elon=Employee()
# elon.details()
p = programmer()
p.details()  # This overwrites
