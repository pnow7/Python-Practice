"""
[입력]
11
1 4 1 2 4 2 4 2 3 4 4
2

11
1 4 1 2 4 2 4 2 3 4 4
5

[출력]
3

0

"""

import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())

count = num.count(check)

count2 = 0

for number in num:
    if (number == check):
        count2 += 1

print(count)
print(count2)