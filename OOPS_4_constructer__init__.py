class employee:
    company = "Google"

    def __init__(self, name, rollno, roomno):
        self.name = name
        self.rollno = rollno
        self.roomno = roomno
        print("Printing Details : \n")

    def getSalary(self):  # employee.getSalary() this is obtined instead of #employee.getSalary(suraj)
        print("Salary is $10000000000")

    def details(self):
        print(
            f"Name of student is {self.name}\nRoll Number of student is {self.rollno}\nClassroom of the student is {self.roomno}")


suraj = employee("Suraj", "20071A3244", "A103")
suraj.details()

# __init__    This is special method
# runs automatically
