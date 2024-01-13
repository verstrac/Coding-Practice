def main():
    check_str = '.,'
    print(palindrome(check_str))


def palindrome(s):
    l_i = 0
    r_i = len(s) - 1
    while l_i < r_i:
        while not s[r_i].isalpha() and not s[r_i].isdigit() and r_i > l_i:
            r_i -= 1
        while not s[l_i].isalpha() and not s[l_i].isdigit() and r_i > l_i:
            l_i += 1
        if s[l_i].lower() != s[r_i].lower():
            return False
        l_i += 1
        r_i -= 1
    return True



if __name__ == '__main__':
    main()
