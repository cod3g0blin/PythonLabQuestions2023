f = open("File/demofile.txt",'r')
#print(f.read())
#print(f.read(6))
#print(f.readline())
#print(f.readline()) #to read the 2nd line

#read using loop
for x in f:
    print(x)

f.close() #good practice to close the file

