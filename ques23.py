#Write a Python function That Accepts a Sentence as Input and Removes All Duplicate Words. Print the Sorted Words
def remove_duplicates_and_print_sorted(sentence):
    words = sentence.split()

    # Remove duplicate words by converting the list to a set
    unique_words = set(words)

    sorted_words = sorted(unique_words)

    for word in sorted_words:
        print(word)
    print(sorted_words[::-1])

sentence = input("Enter a sentence: ")
remove_duplicates_and_print_sorted(sentence)
