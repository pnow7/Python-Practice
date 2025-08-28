"""
UNUCIC는 868242와 같다.

숫자마다 +2

[입력]
WA

UNUCIC

[출력]
13

36

"""

import sys

check = [0] * 27
count = 2

for i in range(1, 27): 
    check[i] = count
    
    if i % 3 == 0:
        count += 1

check[19] = 7
check[22] = 8
check[25] = 9
check[26] = 9
print(*check[1:])

word = list(sys.stdin.readline().strip())

order = 0
sum = 0

for items in word:
    order = ord(items) - 64
    sum += check[order]

print(sum+2)