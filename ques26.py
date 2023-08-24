#Write Python Program to Add two lists using map function.
def add_list(list1,list2):
    return list(map(lambda x,y: x+y,list1,list2))

list1=[1,3,5,7,9]
list2=[2,4,6,8,10]

print(add_list(list1,list2))