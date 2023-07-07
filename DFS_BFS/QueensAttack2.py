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

    # Write your code here
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    queue = []
    obstacles_set = set((obstacle[0],obstacle[1])for obstacle in obstacles)
    #set을 사용하는것이 시간초과 해결의 핵심이었다.
    #  set의 시간 복잡도는 평균적으로 O(1)이며, 최악의 경우에도 O(N)입니다. 이는 해시 테이블을 사용하여 내부적으로 데이터를 저장하기 때문에, 
    # 데이터 조회에 상수 시간이 소요됩니다.
    # 반면에 리스트의 조회 시간 복잡도는 O(N)입니다. 리스트는 데이터를 인덱스에 따라 순차적으로 저장하기 때문에, 
    # 특정 위치에 있는 데이터를 찾기 위해서는 전체 리스트를 탐색해야 합니다. 따라서 리스트의 길이에 비례하는 시간이 소요됩니다.
    count = 0
    #right, left, up, under, cross up, cross down, reverse_cross up, reverse_cross down
    for i in range(8):
        queue.append([r_q,c_q])
        while queue:
            x,y = queue.pop()
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<1 or nx>n or ny<1 or ny>n:
                break
            if (nx,ny) in obstacles_set:
                break
            count += 1
            queue.append([nx,ny])
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
