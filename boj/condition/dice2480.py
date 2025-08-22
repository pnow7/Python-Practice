"""
[입력]
3 3 6

2 2 2

[출력]
1300

12000

"""

a, b, c = map(int, input().split())

if a == b and a == c:
    print(a * 1000 + 10000)
elif a == b:
    print(a * 100 + 1000)
elif a == c:
    print(a * 100 + 1000)
elif b == c:
    print(b * 100 + 1000)
else:
    print(max(a,b,c) *100)