def main():
    print(commonChars(words))


def commonChars(words):
    common_list = []
    len_words = len(words)
    letter_dict = {}
    first_word = words[0]
    for letter in first_word:
        letter_dict[letter] = 1
        for i in range(1, len_words):
            if letter not in words[i]:
                del letter_dict[letter]
                continue
    return common_list


if __name__ == '__main__':
    main()
