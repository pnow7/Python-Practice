"""
[입력]
5
1 1
12 34
5 500
40 60
1000 1000

[출력]
2
46
505
100
2000
"""

import sys

n = int(sys.stdin.readline())

for i in range(n):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)