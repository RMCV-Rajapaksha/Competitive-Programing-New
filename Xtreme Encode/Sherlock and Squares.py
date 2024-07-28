#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Find the smallest integer greater than or equal to sqrt(a)
    start = math.ceil(math.sqrt(a))
    # Find the largest integer less than or equal to sqrt(b)
    end = math.floor(math.sqrt(b))
    
    # The count of integers in the range [start, end] gives the number of square integers
    return max(0, end - start + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
