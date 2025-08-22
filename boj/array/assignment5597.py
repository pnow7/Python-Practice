"""
[입력]
3
1
4
5
7
9
6
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30

[출력]
2
8
"""

import sys

studentnum = []

for i in range(1, 29):
    num = int(sys.stdin.readline())
    studentnum.append(num)

for i in range(1, 31):
    if i not in studentnum:
        print(i)