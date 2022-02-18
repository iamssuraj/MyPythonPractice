import random
def game(comp,k):
    if comp==k:
        return None
    else:
      if(comp=='Rock'):
        if k=='Paper':
            return True
        elif k=='Scissors':
            return False
      elif(comp=='Paper'):
        if k=='Scissors':
            return True
        elif k=='Rock':
            return False
      else:
        if k=='Rock':
            return True
        elif k=='Paper':
            return False
    
b=random.randint(1,3)
if (b==1):
 comp='Rock'
elif(b==2):
  comp='Paper'
else:
   comp='Scissors'
a=int(input("Enter 1 for rock, 2 for paper and 3 for scissors : "))
if a==1:
    k='Rock'
elif a==2:
    k='Paper'
else:
    k='Scisccors'
print("You Chose",k,"and Computer chose",comp)
res=game(comp,k)
if res==None:
    print("Its a tie")
elif res==True:
    print("You Win!")
else:
    print("You Lost!")