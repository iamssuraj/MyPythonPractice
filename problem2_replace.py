# a=input()
# date=input()
# print("Dear, ",a,"\n You are selected\n",date)
# alternative way
message = '''Dear Name,\nGreetings from VNRVJIET.
Your application for VJ Teatro has been shortlisted.
\nFurther details will be sent to you by mail.\nHave a great day ahead!\nDate'''
name = input("Enter your name : ")
date = input("Enter date : ")
message = message.replace("Name", name)
message = message.replace("Date", date)
print(message)
