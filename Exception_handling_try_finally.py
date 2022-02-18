try:
    i=int(input("Enter a number : "))
    c=1/i
except Exception as e:
    print(f"Denominator cant be zero.\n Error is {e}")
    exit()   # even if we exit finally is executed
finally:
    print("We are done")
print("this is executed if condition is only true")