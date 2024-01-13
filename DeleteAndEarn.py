def main():
    print(deleteAndEarn([1,1,1,2,4,5,5,5,6]))


def deleteAndEarn(nums) -> int:
    points = {}
    cache = {}
    maxNumber = 0
    for index, num in enumerate(nums):
        if num > maxNumber:
            maxNumber = num
        if num in points:
            points[num] += num
        if num not in points:
            points[num] = num

    def maxPoints(num):
        if num not in points:
            cache[num] = 0
        if num == 0:
            return 0
        if num == 1:
            if 1 not in cache:
                cache[1] = points[1]
            return cache[1]
        if num in cache:
            return cache[num]
        cache[num] = max(maxPoints(num - 1), maxPoints(num - 2) + points[num])
        return cache[num]

    return maxPoints(maxNumber)


if __name__ == '__main__':
    main()
