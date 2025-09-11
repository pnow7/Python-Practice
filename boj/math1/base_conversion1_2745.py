"""
[입력]
ZZZZZ 36

[출력]
60466175
"""

import sys
import string

alpha_dict = {
    char: ord(char) - 55 for char in string.ascii_uppercase
}

for i in range(10):
    alpha_dict[str(i)] = i

B, N = sys.stdin.readline().split()
N = int(N)

result = 0
reversed_B = reversed(B)

for i, char in enumerate(reversed_B):
    val = alpha_dict[char]
    result += val * (N ** i)

print(result)


"""
N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)
"""