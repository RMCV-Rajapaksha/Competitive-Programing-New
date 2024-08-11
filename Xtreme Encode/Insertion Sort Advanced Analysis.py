#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def merge(list1, list2, counter):
    combined = []

    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            counter += len(list1) - i
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined, counter
    
def divideAndConquer(arr):
    if len(arr) == 1:
        return arr, 0
        
    mid_index = len(arr) // 2
    
    left = divideAndConquer(arr[:mid_index])
    right = divideAndConquer(arr[mid_index:])
    
    return merge(left[0], right[0], left[1] + right[1])
    

def insertionSort(arr):
    return divideAndConquer(arr)[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()