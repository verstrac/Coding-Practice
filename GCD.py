def main():
    print(gcd(105, 5))


def gcd(a, b):
    big_num = max(a, b)
    small_num = min(a, b)

    while small_num > 0:
        remainder = big_num % small_num
        big_num = small_num
        small_num = remainder
    return big_num


if __name__ == '__main__':
    main()
