with open('file.txt', 'r') as f:
    a = f.read()
print(a)
'''
text in the file 
"file.txt" is equal to output here.
NOTE : no need to use the f.close() when using 'with' statement
'''
with open('file.txt', 'w') as f:
    f.write("\nWith Statement\n")