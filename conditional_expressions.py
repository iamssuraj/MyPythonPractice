a = int(input("Enter a number : "))
if(a > 0):
    print(a, "is positive")
elif(a < 0):  # used instead of else if
    print(a, "is negative")
else:
    print(a, "= 0")


# Advanced version of same program with exception handling:
'''
while(True):
    try:
        a=(input("Enter a number : "))
        print("Press q to quit.")
        if(a=='q' or a=='Q'):
            print("Thanks for using the program!.")
            break
        else:
            a=int(a)
            if(a>0):
                print(a,"is positive")
            elif(a<0): #used instead of else if
                print(a,"is negative")
            else:
                print(a,"= 0") 
    except Exception:
        print("Bro, please type a number.")
'''
