f = open("File/demofile.txt","a")
f.write("\nThis statement is appended.")
f.close()

f = open("File/demofile.txt", "r")
print(f.read())