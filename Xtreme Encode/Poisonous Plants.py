#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    n = len(p)
    days = [0] * n
    stack = []

    max_days = 0
    
    for i in range(n):
        max_day = 0
        while stack and p[stack[-1]] >= p[i]:
            max_day = max(max_day, days[stack.pop()])
        
        if stack:
            days[i] = max_day + 1
            max_days = max(max_days, days[i])
        
        stack.append(i)
    
    return max_days

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()