class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,argument):# add is included in the python dictionary
        print("Addition is : ")
        return self.num + argument.num
    def __mul__(self,argument):# mul is included in the python dictionary
        print("Multiplication is : ")
        return self.num * argument.num    
#go to python documentation for operator overloading
a=Number(50)
b=Number(44)
sum = a+b
print(sum)
m=a*b
print(m)