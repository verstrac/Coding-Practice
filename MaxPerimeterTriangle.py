def maximumPerimeterTriangle(sticks):
    # Sort in reverse to find longest stick and loop to find first non-degenerate triangle
    sticks.sort(reverse=True)

    for i in range(len(sticks) - 2):
        long_stick = sticks[i]
        second_longest = sticks[i + 1]
        short_stick = sticks[i + 2]

        if long_stick < (second_longest + short_stick):
            return short_stick, second_longest, long_stick
    return [-1]


print(maximumPerimeterTriangle([1, 1, 1, 3, 3]))