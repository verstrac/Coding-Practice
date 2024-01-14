# Python3 program to calculate the frequency
# of each word in the given string

# Function to print frequency of each word
def print_frequency(word_string):
    words = {}

    # Split words into iterable list, space is default.
    for word in word_string.split():
        if word.lower() in words:
            words[word.lower()] += 1
        else:
            words[word.lower()] = 1

    for word in words.keys():
        print(f'Words frequency for \"{word}\" is {words[word]}')


strr = "Geeks For geeks"
print_frequency(strr)
