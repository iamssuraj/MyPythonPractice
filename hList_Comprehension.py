'''
Syntax:
    newlist = [(expression) for (item) in (iterable) if (condition) == True]
'''





a=[44,213,234,6453,54,76,85,942]
b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)


#shortcut

b=[i for i in a if i%2==0]
print(b)
'''
Explanation:
for loop runs and checks if i%2==0
and stores those values of i
'''
#this is called comprehension
#Dictionary comprehension 
#set comprehension 
#are also present

