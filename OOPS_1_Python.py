# Dry-->Do not repeat yourself
class student:
    fee = 134000
    branch = "CSE"

a = student()
a = input("Enter your name : ")
b = int(input("Enter your rank in EAMCET : "))
if(b < 10000):
    print("Your fee is :", 0)
else:
    print("Your fee is : ", a.fee)
k = input("Are you interested in choosing branch : y/n : ")
print(f"Your name is {a}")
if k == 'y':
    c = input("Enter your preffered branch : ")
    print("Your branch is ", c)
else:
    print("Your branch is : ", a.branch)
