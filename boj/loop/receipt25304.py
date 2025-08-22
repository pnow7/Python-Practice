"""
[입력]
260000
4
20000 5
30000 2
10000 6
5000 8

[출력]
Yes

"""

money = int(input())

n = int(input())

sum = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    sum += a * b

if money == sum:
    print("Yes")
else:
    print("No")
