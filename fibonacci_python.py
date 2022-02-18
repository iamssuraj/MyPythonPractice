a=0
b=1
n=int(input("Enter a number : "))
print("The fibonacci series till",n,"is")
for i in range(0,n):
    print(a)
    c=a+b
    a=b
    b=c
    