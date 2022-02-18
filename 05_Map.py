def square(num):
    return num*num

l1=[1,2,4]

#Method 1 (Long and Traditional)

# l2=[]
# for item in l1:
#     l2.append(square(item))
# print(l2)


#Method 2
print(list(map(square,l1)))
#if list is not included
print(map(square,l1))
#some object is printed

'''
Syntax:
   map(function,input_list)
'''