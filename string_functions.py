# #string functions
# name='''mississippi are are are
#  are are are are 
#  are are testing'''
# # print(len(name))#length of string
# # print(name.endswith("i"))# ends with the given letter or word-->True or false
# # print(name.count("s"))#calculates the frequency of characters  
# # print(name.count("are")) count the occurences of string in given string
# # print(name.capitalize())#capitalizes the 
# # #first letter of string
# print(name.find("mississippi"))#searches and returns position
# #print(name.replace("testing","Suraj"))#replaces all occurences
# #\n can also be used for next line instead of triple quotes


def print_full_name(first, last):
    
    print(f"Hello {first} {last}! You just delved into python.")
    

if __name__ == '__main__':
    first_name =input()
    last_name = input()
    print_full_name(first_name, last_name)
