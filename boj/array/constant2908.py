"""
[입력]
734 893

221 231

[출력]
437

132

"""
import sys

A, B = sys.stdin.readline().split()

reversed_A_str = A[::-1]
reversed_B_str = B[::-1]

reversed_A = int(reversed_A_str)
reversed_B = int(reversed_B_str)

if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)

# print(max(reversed_A, reversed_B))