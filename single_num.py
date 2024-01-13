def main():
    singleNumber([4, 2, 1, 2, 1])


def singleNumber(nums) -> int:
    a = 1
    for i in nums:
        a = a ^ i
    return a



if __name__ == '__main__':
    main()
