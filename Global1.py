a=54 #This is Global variable
def fun1():
    global a #CHANGES THE VALUES OF EVERY 'A'
    print(a)#prints global variable 54
    a=8    #local variable if global keyword is not used 
    print(a) #prints a=8 
fun1()
print(a)#print a=8