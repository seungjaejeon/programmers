#!/bin/python3
#HackerRank
import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n 
#  2. INTEGER m 
#  3. 2D_INTEGER_ARRAY edges 
#  4. INTEGER s 
#
from collections import deque, defaultdict
def bfs(n, m, edges, s):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    distance = [-1] * n
    distance[s-1] = 0
    queue = deque([s])
    while queue:
        nownode = queue.popleft()
        for i in graph[nownode]:
            print(i)
            if distance[i-1]==-1:
                distance[i-1] = distance[nownode-1]+6
                queue.append(i)
    print(distance)
    distance.pop(s-1)
    return distance
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
