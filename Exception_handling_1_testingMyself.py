z=0       
while(True):
    sp=input("Enter the selling price : ")
    try:
        sp=float(sp)
        while(True):
            cp=input("Enter the cost price : ")
            try:                                        #Successful
                cp=float(cp)
                if(sp>cp):
                    print(f"Profit is {sp-cp}")
                elif(cp>sp):
                    print(f"Loss is {cp-sp}")
                else:
                    print("Neither profit nor loss")
                z=1
                break
            except Exception as e1:
                print("Bro, CP should be a number.")
    except Exception as e2:
        print("Bro, SP should be a number.")
    if(z==1):
        break