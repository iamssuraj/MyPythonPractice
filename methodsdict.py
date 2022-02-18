myDictionary={
    "Question":"Value",#comma is important
    "Suraj":"A Coder"
}
print(myDictionary.keys())#prints all the keys
#the type is not list
#we can convert it into list
#print(list(myDictionary.keys()))#prints all the values
# print("\n")
#print(myDictionary.values())#prints all the values
print(myDictionary.items())#gives tuple and prints everything
updateDict={
    "CSBS":"A103",
    "ROLL NO.":"20071A3244",
    "Suraj":"A Magician"#already present above that
    #will be updated
}
myDictionary.update(updateDict)
print(myDictionary)
#important difference b/w [] and .get
#statement below gives None since the text is not present
print(myDictionary.get("Sanganbhatla Suraj"))#doesnt throw error
#print(myDictionary["Sanganbhatla Suraj"])#gives error
#interview question
