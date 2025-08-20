import sys

num_list = []

for i in range(1, 10):
    num = int(sys.stdin.readline())
    num_list.append(num)

max_val = num_list[0]
order = 0

for i in range(len(num_list)):
    if num_list[i] > max_val:
        max_val = num_list[i]
        order = i


print(f"{max_val}\n{order+1}")


