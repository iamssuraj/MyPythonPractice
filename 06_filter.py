def greater(num):
    if num>5:
        return True
    else:
        return False

l=[1,2,3,4,5,6,int('9'),7,89,98]

testlambda = lambda num : num>10
print(list(filter(greater,l)))
#Numbers greater than 5 are filtered and output is same
print(list(filter(testlambda,l)))

'''
Syntax:
    list(filter(function, list))
'''