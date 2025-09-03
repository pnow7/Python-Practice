"""
[입력]
5 4
1 2
3 4
1 4
2 2

[출력]
3 4 1 2 5
"""

import sys

N, M = map(int, sys.stdin.readline().split())

basket_num = [0] * (N + 1)

for item in range(1, N + 1):
    basket_num[item] = item

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    
    start = i
    end = j

    while start < end:
        temp = basket_num[start]
        basket_num[start] = basket_num[end]
        basket_num[end] = temp
        start += 1
        end -= 1

"""
< reveresed 또는 [::-1] 사용 >
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket_num[i:j+1] = reversed(basket_num[i:j+1])
    basket_num[i:j+1] = basket_num[i:j+1][::-1]
"""

print(*basket_num[1:])