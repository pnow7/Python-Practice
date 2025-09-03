"""
바구니 N개

1번 부터 N번가지 번호 매겨져있는 바구니

1번부터 N번까지 번호가 적혀있는 공 

첫째줄 N 입력
둘째 줄 부터 M개의 줄에 걸쳐 공을 넣는 방법

예시 2 5 6 이면 
2번 부터 5번 바구니에 6번 공을 넣음

[입력]
5 4
1 2 3
3 4 4
1 4 1
2 2 2

[출력]
1 2 1 1 0
"""

import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * (N + 1)

for _ in range(M):
    start, end, num = map(int, sys.stdin.readline().split())
    for i in range(start, end + 1):
        basket[i] = num

print(*basket[1:])