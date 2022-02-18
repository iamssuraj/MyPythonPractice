#f=open('file.txt','r')
f=open('file.txt')# r by default
reading=f.read()
# reading=f.read(5)#reads only 5 characters
print(reading)
f.close()