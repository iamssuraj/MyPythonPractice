#enumerate
#recall lists
list1=[44,'20071A3244',"Success",True,"Suraj",'CSBS']

#traditional method
#index=0
#for i in list1:             #bit lengthy method compared to below code
#   print(item,index)
#   index+=1

#shortcut-----> Usage of enumerator

for i,CorrespondingElement in enumerate(list1):
    print(i,CorrespondingElement)