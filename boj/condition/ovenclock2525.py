"""
[입력]
14 30
20

17 40
80

23 48
25

[출력]
14 50

19 0

0 13
"""


hour, min = map(int, input().split())
add_min = int(input())

total_min = (hour * 60) + min 

total_min += add_min

hour = total_min // 60
min = total_min % 60

if hour >= 24:
    hour %= 24

print(hour, min)