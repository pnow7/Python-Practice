### 테스트 코드

import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0] * (N)

for i in range(N):
    basket[i] = basket[i - 1] + 1

num = 0

for _ in range(M):
    first, second = map(int, sys.stdin.readline().split())
    num = basket[first - 1]
    basket[first - 1] = basket[second - 1]
    basket[second - 1] = num

print(*basket)