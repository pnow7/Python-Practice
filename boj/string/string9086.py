"""
[입력]
3
ACDKJFOWIEGHE
O
AB

[출력]
AE
OO
AB
"""

import sys

T = int(sys.stdin.readline())

result = []

for _ in range(T):
    word = sys.stdin.readline().strip()
    str = word[0] + word[len(word)-1]
    result.append(str)

print('\n'.join(result))
