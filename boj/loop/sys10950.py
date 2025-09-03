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

# 배열선언은 [] 선언만 해주면 알아서 자동으로 인식
# _ 쓰는 이유: i 대신 씀, i 쓰면 i 값 인식에 오류가 생길 수 도있음

import sys

n = int(sys.stdin.readline())

inputs = []

for _ in range(n):
    a, b = map(int, input().split())
    inputs.append((a,b))

for a, b in inputs:
    print(a+b)