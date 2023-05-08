#write a program to replace comma-separated words with hyphens and print hyphen-seperated words in ascending order
string=input("Enter a String with comma',' separated words: ")
string=string.lower().replace(",", "-")
print(string)