import sys

N, X = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

result = []

for num in num_list:
    if num < X:
        result.append(num)

print(*result)