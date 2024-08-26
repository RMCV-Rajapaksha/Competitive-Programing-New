
import math
import os
import random
import re
import sys

def boardCutting(cost_y, cost_x):
    data = {'lst': [], 'flag': [True] * (len(cost_x) + len(cost_y))}
    for i in range(len(cost_y)):
        data['lst'].append(cost_y[i])
        data['flag'][i] = False
    for i in range(len(cost_x)):
        data['lst'].append(cost_x[i])

    sorted_keys = sorted(range(len(data['lst'])), key=lambda k: data['lst'][k], reverse=True)
    sorted_data = {key: data[key] for key in data}

    total_cost = 0
    row = 1
    column = 1

    for key in sorted_keys:
        if not sorted_data['flag'][key]:
            row += 1
            total_cost += sorted_data['lst'][key] * column
        else:
            column += 1
            total_cost += sorted_data['lst'][key] * row

    return total_cost % (10**9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        m = int(first_multiple_input[0])

        n = int(first_multiple_input[1])

        cost_y = list(map(int, input().rstrip().split()))

        cost_x = list(map(int, input().rstrip().split()))

        result = boardCutting(cost_y, cost_x)

        fptr.write(str(result) + '\n')

    fptr.close()