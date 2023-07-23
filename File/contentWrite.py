f = open("File/demofile.txt","w")
f.write("Oops i have deleted the whole content...")
f.close()

f = open("File/demofile.txt","r")
print(f.read())