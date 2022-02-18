class Employee:
    company = "Infosys"
    salary = 100
    location = "Delhi"

    # def changeSalary(self,sal):
    #     self.__class__salary=sal   #This is one method of adding '__class__'
    # other method

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changeSalary(444)
print(e.salary)
