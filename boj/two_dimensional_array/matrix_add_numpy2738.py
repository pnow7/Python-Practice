"""
[입력]
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

[출력]
4 4 4
6 6 6
5 6 100
"""

import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())

arr1 = np.array([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
arr2 = np.array([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

result = arr1 + arr2

for row in result:
    print(*row)

