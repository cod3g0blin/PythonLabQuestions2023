# Check if the items in the list are sorted in ascending order or decending order and print suitable message accordingly. Otherwise print "Items are not sorted!"
def checkSortedList(items):
    ascending = all(items[i] <= items[i + 1] for i in range(len(items) - 1))
    descending = all(items[i] >= items[i + 1] for i in range(len(items) - 1))

    if ascending:
        print("The list is in ascending order!")
    elif descending:
        print("The list is in descending order!")
    else:
        print("The list is not sorted!")
    
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

checkSortedList(list)