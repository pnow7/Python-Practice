import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i}: {A+B}")
    print(f"Case #{i}: {A} + {B} = {A+B}")