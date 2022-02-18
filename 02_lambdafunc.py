# def func(a):
#     return a+5


# other way of declaring function ,the lambda function
def func(a): return a+5


x = 44
print(func(x))


# multiple arguments can vbe passed through lambda function

def sum(a, b, c): return a+b+c


print(sum(int(input("Enter number 1 : ")), int(
    input("Enter number 2 : ")), int(input("Enter number 3 : "))))
