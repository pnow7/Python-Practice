"""
바구니 N개
바구니 1번부터 N번까지 번호 있음
바구니에는 공 1개씩 있고 

첫바구니에는 바구니의 번호와 같은 번호가 적힌 공이 있음

앞으로 M번 공을 바꾸려고함

공을 바꿀 바구니 2개 선택
두 바구니에 있는 공을 서로 교환

M번 공을 바꾼 이후 
각 바구니에 어떤 공이 있는지 구하라

첫째 줄 N개의 바구니
둘째 줄 M개의 반복하여 공을 교혼할 방법 주어짐
두 정수 i, j로 이루어져 있고 
i번 바구니와 j번 바구니에 들어있는 공을 교환

[입력]
5 4
1 2
3 4
1 4
2 2

[출력]
3 1 4 2 5
"""

import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * (N + 1)

for i in range(1, N + 1):
    basket[i] = i

for _ in range(M):
    first, second = map(int, sys.stdin.readline().split())
    basket[first], basket[second] = basket[second], basket[first]

print(*basket[1:])