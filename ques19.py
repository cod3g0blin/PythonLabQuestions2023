#write Python function to count the number of occurence of user-entered words in a sentence.
def OccurenceOfUserEnteredWords(sentence):
    count = 0
    sentence=sentence.replace("  ", " ")
    for word in sentence:
        if(word==" "):
            count+=1
    return count

sentence=input("Enter a sentence: ")
print("No. of words = ", (OccurenceOfUserEnteredWords(sentence)+1))