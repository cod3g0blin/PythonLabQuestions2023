#Write Python Program to Conduct a Linear Search for a Given Key Number in the List and Report Success or Failure
def linearSearch(list, key):
    for item in list:
        if list == key :
            return 1
    return 0

list = []
choice = True
while(choice):
    num = input("Enter a number to append in the list: ")
    list.append(num)
    ch = input("Enter Y/y to append more, else enter any number: ")
    if (ch == 'Y' or ch == 'y'):
        continue
    else:
        choice = False
key = input("Enter the key value to be searched for: ")
if (linearSearch(list,key)==1):
    print("Success")
else:
    print("Failure")
