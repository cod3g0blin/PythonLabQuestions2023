#Write Python Code to Sort a Sequence of Names according to Their Alphabetical Order Without Using sort() Function and using sort function
def sortedNames(names):
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            if names[i]>names[j]:
                names[i],names[j] = names[j],names[i]
    return names

namesList = input("Enter names separeted by comma','\n").split(',')
namesList = [name.strip() for name in namesList]
sortNames = sortedNames(namesList)
print("Sorted Names:\n",sortNames)