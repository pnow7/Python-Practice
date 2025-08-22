"""
[입력]
5
1 1
2 3
3 4
9 8
5 2

[출력]
2
5
7
17
7

"""

a = int(input())

for i in range(1, a+1):
    A, B = map(int, input().split())
    print(A+B)