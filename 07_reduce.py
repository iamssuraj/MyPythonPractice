from functools import reduce #necessary to mention

sum = lambda a,b : a+b

l=[1,2,3,4]

#first sum of 1 and 2 is calculated, gives 3
#then 3 is added to 3, gives 6 
#then 6 is added to 4, gives 10
#this is the output
val=reduce(sum,l)
print(val)