m = int(input("rows: "))
n = int(input("columns: "))

a = []

for i in range(m):
    row =[]
    for j in range(n):
    	row.append(int(input('A[' + str(i+1) + ',' + str(j+1) +']: ')))
    a.append(row)

print()

for i in range(m):
    for j in range(n):
        print(a[i][j], end = " ")
    print("\n")