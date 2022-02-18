def calc(str,n1,n2):
    if(str=='+'):
        return n1+n2
    elif(str=='-'):
        return n1-n2
    elif(str=='*'):
        return n1*n2
    elif(str=='/'):
         return n1/n2
        
    
b=float(input("Enter a number : "))
c=float(input("Enter another number : "))
a=input("Enter operator :\n+\n-\n*\n/\n: ")
if(a=='/' and c==0):
    print("Bro, division by zero is not possible.")         
elif(a=='+' or a=='-' or a=='*' or a=='/'):
    print("Result is ",calc(a,b,c))
else:
    print("Bro, what is that operator?")