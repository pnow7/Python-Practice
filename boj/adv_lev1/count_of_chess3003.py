"""
[입력]
0 1 2 2 2 7

2 1 2 1 2 1

[출력]
1 0 0 0 0 1

-1 0 0 1 0 7
"""
import sys

chess = [1, 1, 2, 2, 2, 8]

my_piece = list(map(int, sys.stdin.readline().split()))

for i in range(0, len(my_piece)):
    chess[i] -= my_piece[i]

print(*chess)