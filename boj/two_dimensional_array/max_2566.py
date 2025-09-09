"""
[입력]
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80

[출력]
90
5 7
"""
import sys

arr = []
for _ in range(9):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

tmp = 0
first = 0
second = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > tmp:
            tmp = arr[i][j]
            first = i
            second = j
            
print(tmp)
print(first + 1, second + 1)