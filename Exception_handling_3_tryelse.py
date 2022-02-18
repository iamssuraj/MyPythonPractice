try:
    i=int(input("Enter a number : "))
    c=1/i
except Exception as e:
    print(f"Denominator cant be zero.\n Error is '{e}'")
else:#this is executed if try is passed.
    print("We are successful")