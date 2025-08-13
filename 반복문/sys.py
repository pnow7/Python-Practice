import sys

n = int(sys.stdin.readline())

inputs = []

for _ in range(n):
    a, b = map(int, input().split())
    inputs.append((a,b))

for a, b in inputs:
    print(a+b)