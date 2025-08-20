import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
check = int(sys.stdin.readline())

count = num.count(check)

count2 = 0

for number in num:
    if (number == check):
        count2 += 1

print(count)
print(count2)