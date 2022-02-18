a=0
b=1
c=0
i=2
n=int(input("Enter any decimal number : "))
print(f"The Fibonacci Sequence upto {n} is :")
while(c<n):
      c=a+b
      a=b
      b=c
      a=a
      for i in range(2,n+1):
        if(a%i==0):
            break
      if(i==a):
        print(i)