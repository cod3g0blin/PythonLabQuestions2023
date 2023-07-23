import os
#os.remove("dummyfile.txt")
if(os.path.exists("dummyfile.txt")):
    os.remove("dummyfile.txt")
else:
    print("File doesnot exists")

#to remove folder
os.rmdir("dummyfolder")