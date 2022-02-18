n=int(input("Enter a number : "))
for i in range(2,n):
    if((n%i)==0):
        print(n,"is a non-prime number")
        break

if(n==i+1):
 print(n,"is a prime number")