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

N, M = map(int, sys.stdin.readline().split())

arr1 = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arr1.append(row)

arr2 = []
for _ in range(M):
    col = list(map(int, sys.stdin.readline().split()))
    arr2.append(col)

arr3 = [ [0] * M for _ in range(N) ]

for i in range(N):
    for j in range(M):
        arr3[i][j] = arr1[i][j] + arr2[i][j]

for i in range(N):
    print(*arr3[i])

