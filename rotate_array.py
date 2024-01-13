def main():
    nums = [1,2,3,4,5,6,7]
    k = 3
    nums = rotate(nums, k)
    print(nums)


def rotate(nums, k: int):
    """
    Do not return anything, modify nums in-place instead.
    """
    rotated_array = []
    for j in range(len(nums)):
        rotated_array.append(nums[(j + len(nums) - k) % len(nums)])
    return rotated_array


if __name__ == '__main__':
    main()
