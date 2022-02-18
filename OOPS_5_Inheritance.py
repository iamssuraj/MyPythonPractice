#This uses dry principle
#inheritance is a way of creating new class from
#an exisiting class
class Employee: #base class/parent class
    company="Google"
    def details(self):      
        print("This is an employee")
class programmer(Employee): # child class/ derived class
    lang="Python"
    def getLang(self):
        print(f"The language is {self.lang}")
            
elon=Employee()
elon.details()
print("\n")
p=programmer()
p.getLang()
p.details()
#print(p.company)