#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    #div_sum_pair_count = 0
    #for i in range(n):
    #    for j in range(i + 1, n):
    #        if i < j and (ar[i] + ar[j]) % k == 0:
    #            div_sum_pair_count += 1
    #return div_sum_pair_count
    # Initialize a frequency array for remainders
    freq = [0] * k

    # Initialize a counter for the number of pairs
    count = 0

    for num in ar:
        # Find the complement that, when added to num, would be divisible by k
        complement = (-num % k)

        # Add the frequency of the complement to the count
        count += freq[complement]

        # Update the frequency of the remainder of num
        freq[num % k] += 1

    return count

if __name__ == '__main__':
    print(divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2]))