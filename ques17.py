#Write Python function Po Count the Total Number of Vowels, Consonants and Blanks in a String
def Po(string):
    countVowels=0
    countConsonants=0
    countBlanks=0

    for char in string:
        if char==" ":
            countBlanks+=1
        else:
            if char.lower() in 'aeiou':
                countVowels+=1
            else:
                countConsonants+=1
    return countVowels, countConsonants, countBlanks

string=input("Enter a String: ")
vowels, consonants, blanks = Po(string)
print("Count of Vowels: ",vowels)
print("Count of consonants: ", consonants)
print("Count of Blanks: ", blanks)
