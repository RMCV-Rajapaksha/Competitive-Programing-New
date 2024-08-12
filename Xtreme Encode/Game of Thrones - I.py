#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Create a frequency dictionary
    frequency = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # Count how many characters have an odd frequency
    odd_count = 0
    for count in frequency.values():
        if count % 2 != 0:
            odd_count += 1
    
    # If more than one character has an odd frequency, return "NO"
    if odd_count > 1:
        return "NO"
    
    # Otherwise, return "YES"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
