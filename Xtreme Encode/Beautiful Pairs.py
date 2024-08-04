
import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    from collections import Counter
    
    count_A = Counter(A)
    count_B = Counter(B)
    
    # Calculate the initial number of beautiful pairs
    common_pairs = sum((min(count_A[x], count_B[x]) for x in count_A))
    
    # If all elements in A match with B, changing one element will decrease the count
    if common_pairs == len(A):
        return common_pairs - 1
    else:
        return common_pairs + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()