#multiple inheritance occurs when the 
#child class inherits from more than
#one parent class
#  Example:
class Employee:
    company="VISA"
    eCode=120
    def upgradeCode(self):
        self.eCode=self.eCode+1
class FreeLancer:
    company="Fiverr"
    level=0
    def upgradeLevel(self):
        self.level=self.level+1
class Programmer(Employee,FreeLancer):
    name="Suraj"

p=Programmer()
p.upgradeLevel()
p.upgradeCode()
print(p.level)
print(p.eCode)
print(p.company)
# above we have company in employee and also in Freelancer
# But the ouput is "VISA" ( company of employee) 
# That is because in the 15 the line 
#Employee is first class in Programmer class
