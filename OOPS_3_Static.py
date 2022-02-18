#use of self
class employee:
    company="Google"
    @staticmethod  #if this is used, no need to use self
    def getSalary():  #employee.getSalary() this is obtained instead of #employee.getSalary(suraj)
        print("Salary is $10000000000")

suraj=employee()
suraj.getSalary()

'''
class employee:
    @staticmethod
    def salary():
        print("Salary is 1321313131313124")

suraj=employee()
suraj.salary()
'''