"""
[입력]
5

[출력]
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""

import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

"""
- 오류(끝 쪽 공백은 입력하지 않나봄)

for i in range(1, N + 1):
    print(('*' * (2 * i - 1)).center(2 * N - 1))

for i in range(N - 1, 0, -1):
    print(('*' * (2 * i - 1)).center(2 * N - 1))

"""