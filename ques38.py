'''Program for passing of data validation like password and email'''
import re

def validateEmail(email):
    regex = r'^[a-zA-z0-9.-_+]+@[a-z0-9.-]+\.[a-zA-z]{2,}$'
    if re.match(regex, email):
        return True
    return False
    
def validatePassword(pswd):
    regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(regex,pswd):
        return True
    return False

email = input("Enytr a email: ")
if validateEmail(email):
    print('Valid email')

pswd = "Shubham@487"
if validatePassword(pswd):
    print("valid pswd")

'''Define the pattern: Start by defining the pattern you want to match. For example, if you want to match a string that 
starts with "hello," the pattern would be hello.

Special characters: Regular expressions use special characters to define patterns. Some common special characters are:

. (dot): Matches any character except a newline.
*: Matches zero or more occurrences of the preceding character.
+: Matches one or more occurrences of the preceding character.
?: Matches zero or one occurrence of the preceding character.
\: Escapes a special character, allowing you to match it literally. For example, to match a dot, use \..
[]: Defines a character class, matching any character within the brackets. For example, [aeiou] matches any vowel.
[^]: Defines a negated character class, matching any character NOT within the brackets.
|: Acts as an OR operator, allowing you to match either of the patterns on either side of it.
(): Groups parts of the pattern together.
Quantifiers: You can use quantifiers to specify how many occurrences of a character or group you want to match. For example, 
a{2,4} will match 2 to 4 occurrences of 'a'.

Anchors: Anchors are used to specify where in the string the pattern should match. Common anchors are:

^: Matches the start of the string.
$: Matches the end of the string.
Testing and iterating: After writing your regular expression, you can test it against sample strings to see if it matches the 
desired patterns. Iterate and adjust the pattern as needed to achieve the desired matching behavior.'''