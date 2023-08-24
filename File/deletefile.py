import os
#os.remove("dummyfile.txt")
if(os.path.exists("File/demofile.txt")):
    os.remove("File/demofile.txt")
else:
    print("File doesnot exists")

#to remove folder
os.rmdir("File/dummyfolder")