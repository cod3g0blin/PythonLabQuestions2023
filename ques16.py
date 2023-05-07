#Program to Print the Characters Which Are Common in Two Strings
string1=input("Enter 1st string: ")
string2=input("Enter 2nd string: ")

common=[]
for char in string1:
    if char in string2 and char not in common:
        common.append(char)

if len(common) > 0:
    print("The common characters between the two strings are:")
    for char in common:
        print(char)
else:
    print("There are no common characters between the two strings.")
