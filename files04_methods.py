f = open('file_.txt', 'w')
writing = f.write("New Files testing")
# everything written is overwritten
# in the newfile.txt
# if file is not present it is created
writing = f.write("\nThis comes in the next line")
f.close()