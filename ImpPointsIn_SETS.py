a=set()
a.add(8)#to add elements into set
a.add(1)
a.add(2)
a.add(11)
a.add(22)
print(len(a))#gives length of set 
a.remove(11)#removes 11 from set
#a.remove(15)#15 is not present in the set #throws error
print(a)
# a.pop()#removes a random value from the set
# print(a)
a=a.union({2,4})#union find union of a and numbers given in curly brackets
print(a)
#to find intersection
print("Intersection is ",a.intersection({1,2}))
a.clear()#clears the set
print(a)


