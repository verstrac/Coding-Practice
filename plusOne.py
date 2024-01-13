def main():
    print(plusOne([1, 2, 3, 9]))


def plusOne(digits):
    last_index = len(digits) - 1
    digits[last_index] += 1
    while last_index > 0 and digits[last_index] == 10:
        digits[last_index] = 0
        last_index -= 1
        digits[last_index] += 1
    if last_index == 0 and digits[last_index] == 10:
        digits[last_index] = 0
        digits.insert(0, 1)
    return digits


if __name__ == '__main__':
    main()
