def greet(name):
    print(f"Good morning,{name}")  #only the function will be exported to File2.py

#check File2.py

if __name__=="__main__": 
#because if conditions is false
    #this is executed only if this file is executed
    n=input("Enter your name : ")
    greet(n)           