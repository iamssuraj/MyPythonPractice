a = input("Please enter your name : ")
print("Hi !", a)
b = input("Enter a number : ")
b = int(b)
c = input("Enter another number : ")
c = int(c)
if(b > c):
    print(f"{b}>{c}")  # this is called as #fstring#
else:
    print(c, ">=", b)
