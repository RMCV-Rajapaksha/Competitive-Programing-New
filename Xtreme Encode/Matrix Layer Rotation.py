
import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    rotate = r
    length = min(m, n) // 2
    l, r = 0, n - 1
    row = m - 1
    for i in range(1, length+1):
        count = (r-l)*2 + (row-l)*2
        rot = rotate % count
        for j in range(0, rot):
            temp = matrix[l][l]
            for s1 in range(l, r):
                matrix[l][s1] = matrix[l][s1 + 1]
            for s2 in range(l, row):
                matrix[s2][r] = matrix[s2 + 1][r]
            for s3 in range(r, l, -1):
                matrix[row][s3] = matrix[row][s3-1]
            for s4 in range(row, l+1, -1):
                matrix[s4][l] = matrix[s4 - 1][l]
            matrix[l + 1][l] = temp
        l += 1
        r -= 1
        row -= 1
    for val in matrix:
        print(*val, sep=' ')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)