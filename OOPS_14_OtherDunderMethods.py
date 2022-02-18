class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):  # add is included in the python dictionary
        print("Addition is : ")
        return self.num + num2.num

    def __mul__(self, num2):  # mul is included in the python dictionary
        print("Multiplication is : ")
        return self.num * num2.num

    def __str__(self):  # this is new
        return f"Decimal number {self.num}"

    def __len__(self):  # this is new
        return 1


n = Number(9)
print(n)
print(len(n))
