"""
[입력]
1
1

5
54321

[출력]
1

15
"""

import sys

N = int(sys.stdin.readline())
number = sys.stdin.readline().strip()

sum = 0

for i in range(0, len(number)):
    sum = sum + int(number[i])

print(sum)