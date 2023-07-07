#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    pan = [[0 for i in range(n)]for j in range(n)]
    # Write your code here
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    queue = []
    count = 0
    for i in range(k):
        pan[obstacles[i][0]-1][obstacles[i][1]-1] = 2
    #right, left, up, under, cross up, cross down, reverse_cross up, reverse_cross down
    for i in range(8):
        queue.append([r_q,c_q])
        while queue:
            x,y = queue.pop()
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<1 or nx>n or ny<1 or ny>n:
                break
            if pan[nx-1][ny-1] == 2:
                break
            count += 1
            pan[nx-1][ny-1] = 1

    print(pan)
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
