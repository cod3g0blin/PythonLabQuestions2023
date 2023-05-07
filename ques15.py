#Write Python Code to Determine Whether the Given String Is a Palindrome or Not Using Slicing – Use functions
def isPalindrome(string):
    string=string.lower().replace(" ", "")
    return string == string[::-1]

string=input("Enter a string to check if it is palindrome or not: ")

if(isPalindrome(string)):
    print("The entered string is Palindrome.")
else:
    print("The entered string is not Palindrome.")
