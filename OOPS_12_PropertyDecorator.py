class Employee:
    company = "Microsoft"
    salary = 100 
    salarybonus = 35
    # totalsalary=135

    @property  # this is also called as getter
    def totalsalary(self):
        return self.salary+self.salarybonus

    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val-self.salary


e = Employee()
# print(e.totalsalary)
e.totalsalary = 105

print(e.salary)
print(e.salarybonus)
