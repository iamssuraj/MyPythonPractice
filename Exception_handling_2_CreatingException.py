def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("What is this man?")


a = increment("Suraj")
print(a)