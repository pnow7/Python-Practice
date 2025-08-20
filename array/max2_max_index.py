import sys

num_list = []

for _ in range(9):
    num_list.append(int(sys.stdin.readline()))

max_val = max(num_list)
order = num_list.index(max_val)

print(max_val)
print(order)