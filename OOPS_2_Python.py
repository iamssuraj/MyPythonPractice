# use of self
class employee:
    company = "Google"

    def getSalary(self):
        print("Salary is $10000000000")


suraj = employee()
suraj.getSalary()  # read below comment
'''
this upper line suraj.getSalary() gets converted to 
 employee.getSalary(suraj) here suraj(object) is present so
 self should be included--->here----> def getSalary(here)
'''
# Other way of writing same program

'''

class employee:
    company="Google"
    def getSalary(self):
        print(f"Salary is ${self.salary}")

suraj=employee()
suraj.salary=10000000000
suraj.getSalary()
'''
