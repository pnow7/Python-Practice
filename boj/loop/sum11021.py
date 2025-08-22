"""
[입력]
5
1 1
2 3
3 4
9 8
5 2

[출력]
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7

Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7

"""

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A+B}")
    print(f"Case #{i}: {A} + {B} = {A+B}")