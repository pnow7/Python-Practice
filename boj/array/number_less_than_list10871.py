"""
[입력]
10 5
1 10 4 9 2 3 8 5 7 6

[출력]
1 4 2 3
"""

import sys

N, X = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

result = []

for num in num_list:
    if num < X:
        result.append(num)

print(*result)