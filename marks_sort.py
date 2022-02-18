m1 = int(input("Enter marks in Sub 0 : "))
m2 = int(input("Enter marks in Sub 1 : "))
m3 = int(input("Enter marks in Sub 2 : "))
m4 = int(input("Enter marks in Sub 3 : "))
m5 = int(input("Enter marks in Sub 4 : "))
m6 = int(input("Enter marks in Sub 5 : "))
# input is string convet it into integer
markslist = [m1, m2, m3, m4, m5, m6]
markslist.sort()  # sorting important
print(markslist)