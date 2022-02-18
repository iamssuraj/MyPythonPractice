l = []
n = int(input("Enter number of elements : "))
for i in range(n):
    k = int(input(f"Enter element {i+1} : "))
    l.append(k)

for i in range(0, n):
    print(l[i], end=" ")