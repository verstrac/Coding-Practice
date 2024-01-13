# Python3 program Split camel case
# string to individual strings

def camel_case_split(str):
    words = []

    indexer = 0
    while indexer < len(str):
        if indexer == 0:
            words.append(str[indexer])
        elif str[indexer].isupper() and indexer != 0:
            words.append(str[indexer])
        else:
            words[-1] += str[indexer]
        indexer += 1
    return ' '.join(words)


# Driver code
str = "GeeksForGeeks"
print(camel_case_split(str))