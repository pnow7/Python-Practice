import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

min_val = num_list[0]
max_val = num_list[0]

for num in num_list[1:]:
    if num > max_val:
        max_val = num

    if num < min_val:
        min_val = num

print(min_val, max_val)

"""
5
20 10 35 30 7

min_val = 20
max_val = 20

"""