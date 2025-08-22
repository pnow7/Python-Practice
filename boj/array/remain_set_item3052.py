"""
[입력]
1
2
3
4
5
6
7
8
9
10

39
40
41
42
43
44
82
83
84
85

[출력]
10

6

"""


# set과 len 함수 활용 

import sys

remain_list = []

for _ in range(10):
    num = int(sys.stdin.readline())
    num %= 42
    remain_list.append(num)

result = set(remain_list)

print(len(result))


# 일반적인 방식
remain_list1 = []

for _ in range(10):
    num1 = int(sys.stdin.readline())
    remainder = num1 % 42
    remain_list1.append(remainder)

result1 = []

for item in remain_list1:
    if item not in result1:
        result1.append(item)

print(len(result1))