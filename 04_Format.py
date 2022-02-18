#this is an alternative of fstring
name="Suraj"
RollNo="20071A3244"
a="This is {} and my Roll Number is {} ".format(name,RollNo)
#indexing could be done in brackets and accordingly, the arguments are assigned
#if brackets are kept empty the arguments are assigned in order
b="This is {1} and my name is {0} ".format(name,RollNo)
print(a)
print(b)



#The Other Method
print("\n\n\n\n\n\n")
c="This is {} and my Roll Number is {} "
print(c.format(name,RollNo))